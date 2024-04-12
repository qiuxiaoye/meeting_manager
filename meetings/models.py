from django.db import models

# Create your models here.
from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    prepared_by = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    present = models.BooleanField(default=True)

class Minute(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    content = models.TextField()
