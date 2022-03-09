# Base view Import:
from ..subclasses.base_view import BaseView

# Django view Import:
from django.views.generic import DetailView

# Detail lView class:
class DetailView(BaseView, DetailView):

    # Pre-populated attributes:
    template_name = 'base_views/detail_view.html'
