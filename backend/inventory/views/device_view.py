# Application Import:
from inventory.models.device_model import Device
from inventory.filters.device_filter import DeviceFilter

# Own views models:
from autocli.baseview.views.list_view import ListView
from autocli.baseview.views.detail_view import DetailView
from autocli.baseview.views.update_view import UpdateView
from autocli.baseview.views.delete_view import DeleteView
from autocli.baseview.views.create_view import CreateView

# from django.views.generic.edit import UpdateView

class ModelListView(ListView):

    model = Device
    filterset = DeviceFilter
    plural_panel = True
    list_box_view = True
    list_view = ['hostname', 'device_type', 'ssh_port', 'https_port', 'credential', 'certificate']


class ModelDetailView(DetailView):

    model = Device


class ModelCreateView(CreateView):

    model = Device
    fields = ('active', 'name', 'hostname')
    plural_panel = True


class ModelUpdateView(UpdateView):

    model = Device
    fields = ('active', 'name', 'hostname')


class ModelDeleteView(DeleteView):

    model = Device
