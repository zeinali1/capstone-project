from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    CATEGORY_CHOICES = [
        ("music", "Music"),
        ("sports", "Sports"),
        ("study", "Study"),
        ("tech", "Tech"),
        ("social", "Social"),
        ("other", "Other"),
        ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_events', null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="other")
    
    def __str__(self):
        return self.title

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='registrations', null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, related_name='registrations', null=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.event.title}"
