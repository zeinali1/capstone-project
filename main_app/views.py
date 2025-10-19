from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Count, Q
from django.contrib.auth import login
from django.views import View
from django.core.paginator import Paginator

from .models import Event, Registration
from .forms import EventForm, RegisterForm

# Create your views here.
def home(request):
    current_time = timezone.now()
    query = request.GET.get('q', '').strip()
    date_query = request.GET.get('date', '').strip()
    category = request.GET.get('category', '').strip()

    upcoming_events = Event.objects.filter(event_date__gte=current_time)
    past_events = Event.objects.filter(event_date__lt=current_time)

    if query:
        search_filter = Q(title__icontains=query) | Q(location__icontains=query)
        upcoming_events = upcoming_events.filter(search_filter)
        past_events = past_events.filter(search_filter)

    if date_query:
        upcoming_events = upcoming_events.filter(event_date__date=date_query)
        past_events = past_events.filter(event_date__date=date_query)

    if category:
        upcoming_events = upcoming_events.filter(category=category)
        past_events = past_events.filter(category=category)

    upcoming_events = upcoming_events.annotate(attendee_count=Count('registrations')).order_by('event_date')
    past_events = past_events.annotate(attendee_count=Count('registrations')).order_by('-event_date')

    upcoming_paginator = Paginator(upcoming_events, 5)  # 5 per page
    past_paginator = Paginator(past_events, 5)

    upcoming_page_number = request.GET.get('upcoming_page')
    past_page_number = request.GET.get('past_page')

    upcoming_page = upcoming_paginator.get_page(upcoming_page_number)
    past_page = past_paginator.get_page(past_page_number)

    if request.user.is_authenticated:
        joined_event_ids = Registration.objects.filter(user=request.user).values_list('event_id', flat=True)
        for event in list(upcoming_page) + list(past_page):
            event.is_joined = event.id in joined_event_ids
            event.is_mine = event.created_by == request.user
    else:
        for event in list(upcoming_page) + list(past_page):
            event.is_joined = False
            event.is_mine = False

    return render(request, 'events/home.html', {
        'upcoming_events': upcoming_page,
        'past_events': past_page,
        'query': query,
        'date_query': date_query,
        'category': category,
        'categories': Event.CATEGORY_CHOICES,
    })

@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'events/my_registrations.html', {'registrations': registrations})
    
class SignUpView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        user = self.request.user

        context['is_joined'] = (
            user.is_authenticated
            and Registration.objects.filter(user=user, event=event).exists()
        )
        context['is_creator'] = user.is_authenticated and event.created_by == user
        context['participant_count'] = event.registrations.count()
        return context
    
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')
    
class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.created_by

    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.object.pk})

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        event = self.get_object()
        return event.created_by == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = self.get_object()
        return context

class JoinEventView(LoginRequiredMixin, View):
    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        if event.created_by != request.user:
            Registration.objects.get_or_create(user=request.user, event=event)
        return redirect('event_detail', pk=pk)

class LeaveEventView(LoginRequiredMixin, View):
    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        Registration.objects.filter(user=request.user, event=event).delete()
        return redirect('event_detail', pk=pk)

class MyJoinedEventsView(LoginRequiredMixin, ListView):
    model = Registration
    template_name = 'events/my_joined_events.html'
    context_object_name = 'registrations'

    def get_queryset(self):
        return self.request.user.registrations.select_related('event').order_by('event__event_date')
    