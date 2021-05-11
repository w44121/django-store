import django_filters.rest_framework as filters
from rest_framework.filters import SearchFilter
from .models import Product


class ProductFilter(filters.FilterSet):
    producer = filters.CharFilter(field_name='producer', lookup_expr='title')
    price = filters.NumericRangeFilter(field_name='price', method='filter_by_price')
    socket = filters.CharFilter(field_name='characteristics', lookup_expr='socket')

    class Meta:
        model = Product
        fields = ['producer', 'price', 'socket', ]

    def filter_by_price(self, queryset, name, value):
        min_price = getattr(value, 'start', None)
        max_price = getattr(value, 'stop', None)
        if min_price is None:
            return queryset.filter(price__lte=max_price)
        if max_price is None:
            return queryset.filter(price__gte=min_price)
        return queryset.filter(price__gte=min_price, price__lte=max_price)
