# Application Import:
from inventory.models.device_model import Device
from inventory.models.color_model import Color
from inventory.filters.device_filter import DeviceFilter
from inventory.filters.color_filter import ColorFilter
from inventory.forms.device_form import DeviceForm

# Own views models:
from autocli.baseview.views.list_view import ListView
from autocli.baseview.views.detail_view import DetailView
from autocli.baseview.views.update_view import UpdateView
from autocli.baseview.views.delete_view import DeleteView
from autocli.baseview.views.create_view import CreateView

class DeviceListView(ListView):

    model = Device
    filterset = DeviceFilter
    plural_panel = True
    list_box_view = True
    list_view = ['hostname', 'device_type', 'ssh_port', 'https_port', 'credential', 'certificate']


class ColorListView(ListView):

    model = Color
    filterset = ColorFilter
    plural_panel = True
    list_box_view = True
    list_view = ['hexadecimal']


class DeviceUpdateView(UpdateView):

    model = Color


class DeviceDeleteView(DeleteView):

    model = Color


class DeviceDetailView(DetailView):

    model = Device
    form_class = DeviceForm


class TestCreateView(CreateView):

    model = Device
    form_class = DeviceForm
    plural_panel = True
