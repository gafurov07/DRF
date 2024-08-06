from django.db.models import IntegerChoices
from django_filters.rest_framework import FilterSet, ChoiceFilter

from apps.models import Product


class ProductFilter(FilterSet):
    class Type(IntegerChoices):
        THERE = 3
        SEVEN = 7
        TEN = 10
        FIFTEEN = 15

    type = ChoiceFilter(choices=Type.choices, method='get_type')

    class Meta:
        model = Product
        fields = 'type',

    def get_type(self, queryset, name, value):
        return self.data.created_at
        # return Product.objects.filter(created_at__day__gte=(queryset.created_at.day - value))

# class CategoryFilter(FilterSet):
#     class Meta:
#         model = Category
#         fields = 'name',
