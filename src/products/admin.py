from django.contrib import admin
from .models import (
    Producer,
    Product,
    Category,
)


admin.site.register([
    Producer,
    Product,
    Category,
])
