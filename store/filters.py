import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['engine_capacity_unit', 'details', 'digital', 'image', 'image1', 'image2', 'image3', 
                    'image4', 'image5', 'image6', 'image7', 
                    'image8', 'image9', 'image10']