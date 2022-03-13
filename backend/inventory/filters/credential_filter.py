# Django Import:
from django_filters import FilterSet

# Models Imports:
from inventory.models.credential_model import Credential


# Device filter class:
class ModelFilter(FilterSet):

    class Meta:

        model = Credential
        fields = {
            'active': ['exact'],
            'name': ['contains'],
            'username': ['contains'],
        }
