from rest_framework import serializers
from .models import FeeCategory, Invoice, InvoiceItem, Payment

class FeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeCategory
        fields = '__all__'

class InvoiceItemSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = InvoiceItem
        fields = ['id', 'category', 'quantity', 'unit_price', 'total']

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, )

    class Meta:
        model = Invoice
        fields = ['id', 'student', 'created_at', 'due_date', 'is_paid', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        invoice = Invoice.objects.create(**validated_data)
        for item_data in items_data:
            InvoiceItem.objects.create(invoice=invoice, **item_data)
        return invoice

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'