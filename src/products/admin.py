from django.contrib import admin
from .models import (
    Producer,
    Product,
    Category,
)


admin.site.register([
    Producer,
    Category,
])

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount']
    list_editable = ['price', 'amount']
