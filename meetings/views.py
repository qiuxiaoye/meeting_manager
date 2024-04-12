from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Meeting, Attendee, Minute
from .forms import MeetingForm  # Make sure this line is correct

def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a new URL after POST
    else:
        form = MeetingForm()

    return render(request, 'create_meeting.html', {'form': form})

def roll_call(request, meeting_id):
    # Display attendees and handle marking attendance
    pass

def meeting_minutes(request, meeting_id):
    # Handle the creation of minutes for a meeting
    pass
