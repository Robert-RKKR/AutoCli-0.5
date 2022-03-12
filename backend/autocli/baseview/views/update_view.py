# Base view Import:
from ..subclasses.base_view import BaseView

# Django Import:
from django.shortcuts import redirect

# Django view Import:
from django.views.generic.edit import UpdateView as DjangoView


# Update View class:
class UpdateView(BaseView, DjangoView):

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

        ### Create return URL ###
        # Collect current URL:
        url = self.request.build_absolute_uri()
        # Option one save and create new one:
        if request.POST.get('save_one') is not None:
            self.success_url = url
        # Option one save and edit:
        elif request.POST.get('save_two') is not None:
            self.success_url = url
        # Option one save and return to list view:
        elif request.POST.get('save_three') is not None:
            self.success_url = redirect('device:list').url

        # Return HTML response:
        return super().post(request, *args, **kwargs)
