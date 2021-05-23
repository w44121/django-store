from django.contrib import admin
from .models import Order, OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price', 'is_paid', 'is_active']
    list_editable = ['is_paid', 'is_active']
