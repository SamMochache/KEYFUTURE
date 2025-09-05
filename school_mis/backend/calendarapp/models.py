from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    event_type = models.CharField(max_length=100, default='General')

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"