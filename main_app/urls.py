from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', views.home, name='home'),
   path('auth/signup/',views.SignUpView.as_view(), name='signup'),
   path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('auth/login/', auth_views.LoginView.as_view(), name='login'),

   path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
   path('event/new/', views.EventCreateView.as_view(), name='create_event'),
   path('event/<int:pk>/edit/', views.EventUpdateView.as_view(), name='edit_event'),
   path('event/<int:pk>/delete/', views.EventDeleteView.as_view(), name='delete_event'),
   path('event/<int:pk>/join/', views.JoinEventView.as_view(), name='join_event'),
   path('event/<int:pk>/leave/', views.LeaveEventView.as_view(), name='leave_event'),

   path('my-events/', views.MyJoinedEventsView.as_view(), name='my_joined_events'),
   path('my-registrations/', views.my_registrations, name='my_registrations'),

   path('profile/', views.ProfileDetailView.as_view(), name='profile'),
   path('profile/edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),

   path('notifications/', views.AllNotificationsView.as_view(), name='all_notifications'),
   path('notifications/read/<int:pk>/', views.mark_notification_read, name='mark_notification_read'),
   path('notifications/check/', views.check_new_notifications, name='check_new_notifications'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)