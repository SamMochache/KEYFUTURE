from rest_framework import viewsets,permissions
from .models import Exam, GradeEntry
from .serializers import ExamSerializer, GradeEntrySerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated]

class GradeEntryViewSet(viewsets.ModelViewSet):
    queryset = GradeEntry.objects.all()
    serializer_class = GradeEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

