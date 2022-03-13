# Application Import:
from inventory.models.credential_model import Credential
from inventory.filters.credential_filter import ModelFilter

# Own views models:
from autocli.baseview.views.list_view import ListView
from autocli.baseview.views.detail_view import DetailView
from autocli.baseview.views.update_view import UpdateView
from autocli.baseview.views.delete_view import DeleteView
from autocli.baseview.views.create_view import CreateView


# Local constans:
MAIN_MODEL = Credential
FILTER_SET = ModelFilter
LIST_VIEW = ['username']
EDIT_FIELDS = ('active', 'name', 'username')


# All default models views:
class ModelListView(ListView):

    model = MAIN_MODEL
    filterset = FILTER_SET
    list_box_view = True
    list_view = LIST_VIEW


class ModelDetailView(DetailView):

    model = MAIN_MODEL


class ModelCreateView(CreateView):

    model = MAIN_MODEL
    fields = EDIT_FIELDS


class ModelUpdateView(UpdateView):

    model = MAIN_MODEL
    fields = EDIT_FIELDS


class ModelDeleteView(DeleteView):

    model = MAIN_MODEL
