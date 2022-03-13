# Django language import:
from django.utils.translation import gettext_lazy as _

# Base view Import:
from ..subclasses.base_view import BaseView

# Django view Import:
from django.views.generic import DetailView as DjangoView

# Detail lView class:
class DetailView(BaseView, DjangoView):

    # Pre-populated attributes:
    template_name = 'base_views/detail_view.html'
    singular = True

    def get(self, request, *args, **kwargs):
        """ Overwrite get function. """

        # Inherit functionality from get function:
        super().get(request, *args, **kwargs)
        # Collect context data:
        context = self.get_context_data()
        # Submit object PK to HTML template:
        context['object_pk'] = self.object.pk
    
        # Return HTML response:
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        """ Overwrite post function. """

        # Inherit functionality from get function:
        super().get(request, *args, **kwargs)
        # Collect context data:
        context = self.get_context_data()
        # Submit object PK to HTML template:
        context['object_pk'] = self.object.pk

        # Return HTML response:
        return super().post(request, *args, **kwargs)
