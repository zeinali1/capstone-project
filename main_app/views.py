from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login
from django.views import View

from .models import Event, Registration
from .forms import EventForm, RegisterForm

# Create your views here.
def home(request):
    current_time = timezone.now()
    upcoming_events = Event.objects.filter(event_date__gte=current_time).order_by('event_date')
    past_events = Event.objects.filter(event_date__lt=current_time).order_by('-event_date')

    if request.user.is_authenticated:
        joined_event_ids = Registration.objects.filter(user=request.user).values_list('event_id', flat=True)
        for event in upcoming_events:
            event.is_joined = event.id in joined_event_ids
            event.is_mine = event.created_by == request.user
        for event in past_events:
            event.is_joined = event.id in joined_event_ids
            event.is_mine = event.created_by == request.user
    else:
        for event in upcoming_events:
            event.is_joined = False
            event.is_mine = False
        for event in past_events:
            event.is_joined = False
            event.is_mine = False

    return render(request, 'events/home.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
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
    
class PastEventsView(ListView):
    model = Event
    template_name = 'events/past_events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(event_date__lt=timezone.now()).order_by('-event_date')