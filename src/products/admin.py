from django.contrib import admin
from django.utils.html import mark_safe
from .models import (
    Producer,
    Product,
    Category,
    Image,
)


admin.site.register([
    Producer,
    Category,
])


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def show_image(self, obj):
        return mark_safe(f'<img src="{obj.image.all()[0]}" width="100" height="100" />')

    show_image.short_description = 'image'

    list_display = ['title', 'category', 'producer', 'show_image', 'price', 'amount']
    search_fields = ['title', 'category__title']
    list_editable = ['price', 'amount']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
