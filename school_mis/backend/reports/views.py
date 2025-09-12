from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from students.models import Student
from exams.models import GradeEntry
from attendance.models import AttendanceStatus, Attendance
from fees.models import Invoice

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_report(request, student):
    try:
        student_instance = Student.objects.get(id=student)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    grades = GradeEntry.objects.filter(student_id=student_instance.id)
    if not grades.exists():
        return Response({"error": f"No grades found for student {student_instance.id}"}, status=404)

    avg_grade = sum(grade.score for grade in grades) / grades.count()
    return Response({
        "student_id": student_instance.id,
        "average_grade": avg_grade,
        "grades": [{"exam": grade.exam.name, "score": grade.score, "subject": grade.subject.name, "grade": grade.grade()} for grade in grades]
    })
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def attendance_report(request, student):
    try:
        student_instance = Student.objects.get(id=student)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    attendance_records = Attendance.objects.filter(student_id=student_instance.id)
    if not attendance_records.exists():
        return Response({"error": f"No attendance records found for student {student_instance.id}"}, status=404)

    total_days = attendance_records.count()
    present_days = attendance_records.filter(status=AttendanceStatus.PRESENT).count()
    absent_days = attendance_records.filter(status=AttendanceStatus.ABSENT).count()
    excused_days = attendance_records.filter(status=AttendanceStatus.EXCUSED).count()
    attendance_percentage = (present_days / total_days) * 100 if total_days > 0 else 0

    return Response({
        "student_id": student_instance.id,
        "total_days": total_days,
        "present_days": present_days,
        "absent_days": absent_days,
        "excused_days": excused_days,
        "attendance_percentage": attendance_percentage
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fee_report(request, student):
    try:
        student_instance = Student.objects.get(id=student)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    invoices = Invoice.objects.filter(student_id=student_instance.id)
    if not invoices.exists():
        return Response({"error": f"No invoices found for student {student_instance.id}"}, status=404)

    total_fees = sum(invoice.amount for invoice in invoices)
    total_paid = sum(invoice.paid_amount for invoice in invoices)
    total_due = total_fees - total_paid

    return Response({
        "student_id": student_instance.id,
        "total_fees": total_fees,
        "total_paid": total_paid,
        "total_due": total_due,
        "invoices": [{"id": invoice.id, "amount": invoice.amount, "paid_amount": invoice.paid_amount, "due_date": invoice.due_date} for invoice in invoices]
    })