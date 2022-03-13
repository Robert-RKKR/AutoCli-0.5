# Application Import:
from inventory.models.color_model import Color
from inventory.filters.color_filter import ModelFilter

# Own views models:
from autocli.baseview.views.list_view import ListView
from autocli.baseview.views.detail_view import DetailView
from autocli.baseview.views.update_view import UpdateView
from autocli.baseview.views.delete_view import DeleteView
from autocli.baseview.views.create_view import CreateView


# Local constans:
MAIN_MODEL = Color
FILTER_SET = ModelFilter
LIST_VIEW = ['hexadecimal']
EDIT_FIELDS = ('active', 'name', 'hexadecimal', 'devices', 'folders', 'credentials')


# All default models views:
class ModelListView(ListView):

    model = MAIN_MODEL
    filterset = FILTER_SET
    plural_panel = True
    list_box_view = True
    list_view = LIST_VIEW


class ModelDetailView(DetailView):

    model = MAIN_MODEL


class ModelCreateView(CreateView):

    model = MAIN_MODEL
    fields = EDIT_FIELDS
    plural_panel = True


class ModelUpdateView(UpdateView):

    model = MAIN_MODEL
    fields = EDIT_FIELDS


class ModelDeleteView(DeleteView):

    model = MAIN_MODEL
