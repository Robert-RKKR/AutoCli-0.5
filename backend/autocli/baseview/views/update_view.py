# Base view Import:
from ..subclasses.base_view import BaseView

# Django view Import:
from django.views.generic.edit import UpdateView as DjangoView


# Update View class:
class UpdateView(BaseView, DjangoView):

    # Pre-populated attributes:
    success_url = '/'