from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'location', 'category']
        widgets = {
            'event_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                    'placeholder': 'Select date and time',
                }
            ),
        }

    def clean_event_date(self):
        event_date = self.cleaned_data['event_date']
        instance = getattr(self, 'instance', None)

        if instance and instance.pk and event_date == instance.event_date:
            return event_date

        if event_date < timezone.now():
            raise forms.ValidationError("Event date cannot be in the past.")
        return event_date


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
