from django.urls import path
from . import views


urlpatterns = [
   path('', views.HomeView.as_view(), name='home'),
   path('auth/signup/',views.SignUpView.as_view(), name='signup'),
   path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
   path('event/new/', views.EventCreateView.as_view(), name='create_event'),
   path('event/<int:pk>/edit/', views.EventUpdateView.as_view(), name='edit_event'),
   path('event/<int:pk>/delete/', views.EventDeleteView.as_view(), name='delete_event'),
   path('event/<int:pk>/join/', views.JoinEventView.as_view(), name='join_event'),
]