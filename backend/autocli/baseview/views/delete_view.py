# Django language import:
from django.utils.translation import gettext_lazy as _

# Base view Import:
from ..subclasses.base_view import BaseView

# Django Import:
from django.urls import reverse_lazy


# Django view Import:
from django.views.generic.edit import DeleteView as DjangoView


# Delete View class:
class DeleteView(BaseView, DjangoView):

    # Pre-populated attributes:
    template_name = 'base_views/delete_view.html'
    singular = True
    success_url = '/'
    page_name_action = _('Delete')

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
        # Create return URL:
        requested_site = self._collect_class_name() + ':list'
        self.success_url = reverse_lazy(requested_site)

        # Return HTML response:
        return super().post(request, *args, **kwargs)
