from django.db import models
from django.conf import settings

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='classrooms', blank=True, limit_choices_to={'role': 'TEACHER'})

class Meta:
        unique_together = ('name', 'section')

def __str__(self):
        return f"{self.name} - {self.section}"

class Subject(models.Model):
       name = models.CharField(max_length=100)
       code = models.CharField(max_length=20, unique=True)
       classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='subjects')
       teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='subjects', blank=True, limit_choices_to={'role': 'TEACHER'})

       def __str__(self):
           return f"{self.name} ({self.code})"