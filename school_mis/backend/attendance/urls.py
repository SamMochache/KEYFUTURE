from django.urls import path
from .views import AttendanceStatusView

urlpatterns = [
    path('status-options/', AttendanceStatusView.as_view(), name='attendance-status-options'),
]
