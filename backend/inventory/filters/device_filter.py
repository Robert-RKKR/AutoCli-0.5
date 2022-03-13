# Django Import:
from django_filters import FilterSet

# Models Imports:
from inventory.models.device_model import Device


# Device filter class:
class ModelFilter(FilterSet):

    class Meta:

        model = Device
        fields = {
            'active': ['exact'],
            'name': ['contains'],
            'hostname': ['contains'],
            'credential': ['exact'],
            'device_type': ['exact'],
            'ssh_status': ['exact'],
            'https_port': ['exact'],
        }
