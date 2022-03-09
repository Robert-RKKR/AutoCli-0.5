# Base view Import:
from ..subclasses.base_view import BaseView

# Django view Import:
from django.views.generic.edit import UpdateView


# Update View class:
class UpdateView(BaseView, UpdateView):

    # Pre-populated attributes:
    success_url = '/'