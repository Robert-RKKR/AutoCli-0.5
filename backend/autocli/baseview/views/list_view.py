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

        self.page_data['output'] = self._collect_get_parameters(request)

        return render(request, self._get_attribute(self.template, 'base_views/list_view.html'), self.page_data)
