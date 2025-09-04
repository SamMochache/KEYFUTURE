from django.db import models
from django.conf import settings
from academics.models import Classroom

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile', limit_choices_to={'role': 'STUDENT'})
    admission_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    guardian = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='wards', limit_choices_to={'role': 'GUARDIAN'})
    current_classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    date_admitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.admission_number})"