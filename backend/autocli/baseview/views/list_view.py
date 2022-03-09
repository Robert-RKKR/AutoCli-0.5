# Python Import:
import re

# Base view Import:
from ..subclasses.base_view import BaseView

# Django view Import:
from django.views.generic import ListView


# List View class:
class ListView(BaseView, ListView):

    # Blank value attributes:
    filterset = None

    # Pre-populated attributes:
    template_name = 'base_views/list_view.html'
    paginate_by = 5

    def get_queryset(self):
        """ Overwrite get_queryset function. """

        # Inherit functionality from get_queryset function:
        queryset = super().get_queryset()
        # Filter results based on provided filter class:
        self.filter_results = self.filterset(self.request.GET, queryset=queryset)
        # Set value of no_search_result variable:
        self.no_search_result = True if not self.filter_results.qs else False

        # Return serache results:
        return self.filter_results.qs.distinct()

    def get_context_data(self, **kwargs):
        """ Overwrite get_context_data function. """

        # Inherit functionality from get_context_data function:
        context = super().get_context_data(**kwargs)
        # Submit query string to HTML template:
        context['query_string'] = self.get_query_string()
        # Submit no_search_result variable to HTML template:
        context['no_search_result'] = self.no_search_result
        # Submit filter class to HTML template:
        context['filter'] = self.filter_results

        # Return context data:
        return context

    def get_query_string(self):
        """ Returns url query string base on get request url. """

        # Collect URL query string from http request:
        query_string = self.request.META.get('QUERY_STRING', '')
        # Validate collected query string to remove page value:
        validated_query_string = '&'.join([x for x in re.findall(
            r'(\w*=\w{1,})', query_string) if not 'page=' in x])

        # Return validated query string with & symbol or blank string:
        return '&' + validated_query_string if (validated_query_string and not self.no_search_result) else ''
    
    # GET request response page:
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

    def _collect_panel_data(self):
        """ Genetate panel data. """

        # 
        collected_panel_data = []
        model_name = self.model._meta.object_name.lower() + '-create'

        if self.plural_panel is True:
            data = {
                'ico': 'create',
                'link': model_name
            }
            collected_panel_data.append(data)

        return collected_panel_data
