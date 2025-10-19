from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('auth/signup/',views.SignUpView.as_view(), name='signup'),

   path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
   path('event/new/', views.EventCreateView.as_view(), name='create_event'),
   path('event/<int:pk>/edit/', views.EventUpdateView.as_view(), name='edit_event'),
   path('event/<int:pk>/delete/', views.EventDeleteView.as_view(), name='delete_event'),
   path('event/<int:pk>/join/', views.JoinEventView.as_view(), name='join_event'),
   path('event/<int:pk>/leave/', views.LeaveEventView.as_view(), name='leave_event'),

   path('my-events/', views.MyJoinedEventsView.as_view(), name='my_joined_events'),

   path('my-registrations/', views.my_registrations, name='my_registrations'),
]