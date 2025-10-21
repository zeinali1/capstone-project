from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from main_app.models import Event, Notification

class Command(BaseCommand):
    help = "Send event reminder emails to attendees 24 hours before the event."

    def handle(self, *args, **kwargs):
        now = timezone.now()
        upcoming_events = Event.objects.filter(event_date__range=(now, now + timezone.timedelta(hours=24)))

        for event in upcoming_events:
            registrations = event.registrations.select_related('user')
            for reg in registrations:
                user = reg.user
                send_mail(
                    subject=f"Reminder: {event.title} is tomorrow!",
                    message=(
                        f"Hi {user.username},\n\n"
                        f"Don't forget your event '{event.title}' on "
                        f"{event.event_date.strftime('%b %d, %Y at %H:%M')}.\n"
                        f"Location: {event.location}\n\n"
                        f"– EventEase Team"
                    ),
                    from_email='noreply@eventease.com',
                    recipient_list=[user.email],
                    fail_silently=True,
                )

                Notification.objects.create(
                    user=user,
                    message=f"Reminder: {event.title} starts soon!"
                )

        self.stdout.write(self.style.SUCCESS("✅ Event reminders sent successfully."))
