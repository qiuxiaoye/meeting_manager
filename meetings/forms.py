from django.forms import ModelForm
from .models import Meeting

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'date', 'time_start', 'time_end', 'prepared_by', 'location']
