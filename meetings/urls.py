from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_meeting, name='create_meeting'),
    path('roll_call/', views.roll_call, name='roll_call'),
    # path('roll_call/<int:meeting_id>/', views.roll_call, name='roll_call'),
    path('minutes/<int:meeting_id>/', views.meeting_minutes, name='meeting_minutes'),
]
