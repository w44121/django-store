from django.contrib import admin
from django.utils.html import mark_safe
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
    def show_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')

    show_image.short_description = 'image'

    list_display = ['title', 'category', 'producer', 'show_image', 'price', 'amount']
    search_fields = ['title', 'category__title']
    list_editable = ['price', 'amount']
