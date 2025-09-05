from rest_framework import viewsets, permissions
from .models import FeeCategory, Invoice, Payment
from .serializers import FeeCategorySerializer, InvoiceSerializer, PaymentSerializer

class FeeCategoryViewSet(viewsets.ModelViewSet):
    queryset = FeeCategory.objects.all()
    serializer_class = FeeCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.prefetch_related('items').all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.prefetch_related('invoice').all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]