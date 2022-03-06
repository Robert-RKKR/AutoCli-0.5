# Django Imports:
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, get_object_or_404

# Base view Import:
from ..baseview import BaseView


# List View class:
class ListView(BaseView):

    # GET request response page:
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        # Generate default page name if not provided:
        self.page_data['page_name'] = self._get_page_name(_('Display all'), True)

        # Return all collected objects:
        self.page_data['objects'] = self._collect_objects(request)

        # Collect all filtered value used to create template filter options:
        self._get_filter_template()


        self.page_data['output'] = self.collect_model_attributes_names()

        return render(request, self._get_attribute(self.template, 'base_views/list_view.html'), self.page_data)
