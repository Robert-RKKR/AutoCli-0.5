# Base view Import:
from ..subclasses.base_view import BaseView

# Django Import:
from django.shortcuts import redirect


# Django view Import:
from django.views.generic.edit import DeleteView as DjangoView


# Delete View class:
class DeleteView(BaseView, DjangoView):

    # Pre-populated attributes:
    template_name = 'base_views/delete_view.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        """ Overwrite post function. """

        # Inherit functionality from get function:
        super().get(request, *args, **kwargs)
        # Collect context data:
        context = self.get_context_data()
        # Add panel data to HTML template:
        context['panel'] = self._collect_panel_data()

        # Create return URL:
        self.success_url = redirect('device:list').url

        # Return HTML response:
        return super().post(request, *args, **kwargs)