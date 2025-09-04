from django.contrib.auth.models import AbstractUser
from django.db import models

class Roles(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    TEACHER = 'TEACHER', 'Teacher'
    STUDENT = 'STUDENT', 'Student'
    PARENT = 'PARENT', 'Parent'
    STAFF = 'STAFF', 'Staff'

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=Roles.choices)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"