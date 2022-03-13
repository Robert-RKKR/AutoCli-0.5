# Base view Import:
from ..subclasses.base_view import BaseView

# Django Import:
from django.urls import reverse_lazy

# Django view Import:
from django.views.generic.edit import UpdateView as DjangoView


# Update View class:
class UpdateView(BaseView, DjangoView):

    # Pre-populated attributes:
    template_name = 'base_views/create_view.html'
    singular_panel = True
    success_url = '/'

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

        ### Create return URL ###
        # Collect current URL:
        url = self.request.build_absolute_uri()
        # Option one save and create new one:
        if request.POST.get('save_one') is not None:
            requested_site = self._collect_class_name() + ':create'
            self.success_url = reverse_lazy(requested_site)
        # Option one save and edit:
        elif request.POST.get('save_two') is not None:
            self.success_url = url
        # Option one save and return to list view:
        elif request.POST.get('save_three') is not None:
            requested_site = self._collect_class_name() + ':list'
            self.success_url = reverse_lazy(requested_site)

        # Return HTML response:
        return super().post(request, *args, **kwargs)
