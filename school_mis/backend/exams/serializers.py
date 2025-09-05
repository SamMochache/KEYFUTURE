from rest_framework import serializers
from .models import Exam, GradeEntry

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class GradeEntrySerializer(serializers.ModelSerializer):
    grade = serializers.ReadOnlyField()

    class Meta:
        model = GradeEntry
        fields = '__all__'