# Django Import:
from django_filters import FilterSet

# Models Imports:
from inventory.models.color_model import Color


# Device filter class:
class ColorFilter(FilterSet):

    class Meta:

        model = Color
        fields = {
            'active': ['exact'],
            'name': ['contains'],
            'hexadecimal': ['contains'],
            'devices': ['exact'],
            'folders': ['exact'],
            'credentials': ['exact'],
        }
