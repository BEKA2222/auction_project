from django_filters import FilterSet
from .models import CarModel


class ProductFilter(FilterSet):
    class Meta:
        model = CarModel
        fields = {
            'car_model': ['exact'],
            'price': ['gt', 'lt']
        }