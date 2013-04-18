from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    event_creator = models.ForeignKey(User)
    event_name = models.CharField(max_length=128)
    event_date = models.DateTimeField('Event date')
    event_creation = models.DateTimeField('Date created')
    event_text = models.CharField(max_length=4096)
