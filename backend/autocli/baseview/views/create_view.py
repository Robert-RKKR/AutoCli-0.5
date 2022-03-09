# Base view Import:
from ..subclasses.base_view import BaseView

# Django view Import:
from django.views.generic.edit import CreateView


# Create View class:
class CreateView(BaseView, CreateView):

    # Pre-populated attributes:
    template_name = 'base_views/create_view.html'
    success_url = '/'
