# Django Imports:
from django.forms import ModelForm

# Models Imports:
from inventory.models.device_model import Device


# Device filter class:
class DeviceForm(ModelForm):

    class Meta:
        model = Device
        fields = ('active', 'name', 'hostname')
