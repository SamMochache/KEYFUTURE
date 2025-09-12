from django.contrib import admin
from .models import FeeCategory, Invoice, Payment

admin.site.register(FeeCategory)
admin.site.register(Invoice)
admin.site.register(Payment)
