# Application Import:
from inventory.models.device_model import Device
from inventory.filters.device_filter import DeviceFilter
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


class DeviceDetailView(DetailView):

    model = Device


class TestCreateView(CreateView):

    model = Device
    form_class = DeviceForm
    plural_panel = True
