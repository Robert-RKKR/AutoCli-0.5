# Base view Import:
from ..subclasses.base_view import BaseView

# Django view Import:
from django.views.generic.edit import CreateView


# Create View class:
class CreateView(BaseView, CreateView):

    # Pre-populated attributes:
    template_name = 'base_views/create_view.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        """ Overwrite get function. """

        # Inherit functionality from get function:
        super().get(request, *args, **kwargs)
        # Collect context data:
        context = self.get_context_data()
        # Add panel data to HTML template:
        context['panel'] = self._collect_panel_data()
        # Return HTML response:
        return self.render_to_response(context)
