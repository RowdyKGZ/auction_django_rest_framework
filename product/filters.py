import django_filters

from product.models import Product


class ProductFilter(django_filters.FilterSet):
    """Фильтрация"""
    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ('price_from', 'price_to')
