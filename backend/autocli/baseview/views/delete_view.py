# Base view Import:
from ..subclasses.base_view import BaseView

# Django view Import:
from django.views.generic.edit import DeleteView


# Delete View class:
class DeleteView(BaseView, DeleteView):

    pass
