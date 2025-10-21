from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from .models import Event, Notification

@shared_task
def send_event_reminders():
    now = timezone.now()
    upcoming_events = Event.objects.filter(event_date__range=(now, now + timezone.timedelta(hours=24)))

    for event in upcoming_events:
        for attendee in event.attendees.all():
            send_mail(
                subject=f"Reminder: {event.title} is tomorrow!",
                message=f"Hi {attendee.username},\n\nDon't forget your event '{event.title}' on {event.event_date.strftime('%b %d, %Y at %H:%M')}.\nLocation: {event.location}\n\nEventEase",
                from_email='noreply@eventease.com',
                recipient_list=[attendee.email],
                fail_silently=True,
            )

            Notification.objects.create(
                user=attendee,
                message=f"Reminder: {event.title} starts soon!"
            )
