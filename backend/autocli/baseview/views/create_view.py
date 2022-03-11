# Base view Import:
from ..subclasses.base_view import BaseView

# Django view Import:
from django.views.generic.edit import CreateView as DjangoView


# Create View class:
class CreateView(BaseView, DjangoView):

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

    def post(self, request, *args, **kwargs):
        """ Overwrite post function. """

        # Inherit functionality from get function:
        super().get(request, *args, **kwargs)
        # Collect context data:
        context = self.get_context_data()
        # Add panel data to HTML template:
        context['panel'] = self._collect_panel_data()
        # Change successful URL:
        print('----->', self.request.META.get('url'))
        self.success_url = self.request.get_raw_uri()
        # Return HTML response:
        return super().post(request, *args, **kwargs)
