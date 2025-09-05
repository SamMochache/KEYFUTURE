from django.db import models
from academics.models import Subject, Classroom
from students.models import Student

class Exam(models.Model):
    name = models.CharField(max_length=100)
    term = models.CharField(max_length=50)
    date = models.DateField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.term}"
    
class GradeEntry(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('exam', 'student', 'subject')

    @property
    def grade(self):
        m=float(self.marks)
        if m >= 90:
            return 'A+'
        elif m >= 80:
            return 'A'
        elif m >= 70:
            return 'B'
        elif m >= 60:
            return 'C'
        elif m >= 50:
            return 'D'
        else:
            return 'F'