# Django Import:
from django_filters import FilterSet

# Models Imports:
from inventory.models.folder_model import Folder


# Device filter class:
class ModelFilter(FilterSet):

    class Meta:

        model = Folder
        fields = {
            'active': ['exact'],
            'name': ['contains'],
            'devices': ['exact'],
        }
