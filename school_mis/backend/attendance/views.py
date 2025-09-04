from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import AttendanceStatus

class AttendanceStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = [
            {'value': status.value, 'label': status.label}
            for status in AttendanceStatus
        ]
        return Response(data)
