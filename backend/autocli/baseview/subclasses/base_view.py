# Python Import:
import re

# Django Import:
from django.views import View


# Create View class:
class BaseView(View):

    singular_panel = None
    plural_panel = None
    list_box_view = None

    def get_context_data(self, **kwargs):
        """ Overwrite get_context_data function. """

        # Inherit functionality from get_context_data function:
        context = super().get_context_data(**kwargs)
        # Submit current URL request to HTML template:
        url = self.request.build_absolute_uri()
        context['current_url'] = url
        # Submit carrent URL with out display request to HTML template:
        context['current_url_no_display'] = self._no_display_url(url)
        # Submit display_version value to HTML template:
        context['display_version'] = self._chaeck_display_version(url)

        # Return context data:
        return context

    def _chaeck_display_version(self, url):
        """ Check display version based on provided URL or default value. """

        # Declare return value:
        return_value = None
        # Search URL to find all query values:
        query_values = re.findall(r'(\w*=\w{1,})', url)
        # Collect display value from all query values:
        for row in query_values:
            if 'display' in row:
                try:
                    return_value = int(row.split('=')[1])
                except:
                    return_value = None

        # Use default value if value was not provided by URL
        # or value is nat valid:
        if return_value is None:
            return_value = 1

        # Return display query value:
        return return_value

    def _no_display_url(self, url):
        """ Return URL with out display query. """

        # Validate collected query string to remove page value:
        validated_query_string = '&'.join([x for x in re.findall(
            r'(\w*=\w{1,})', url) if not 'display=' in x])

        # Return validated query string with ? symbol or blank string:
        return '?' + validated_query_string

    def _collect_panel_data(self):
        """ Genetate panel data. """

        # Return panel dictionary:
        collected_panel_data = {
            'action_objects': [],
            'list_box_view': False
        }
        # 
        model_name = self.model._meta.object_name.lower() + '-create'

        if self.plural_panel is True:
            data = {
                'ico': 'create',
                'link': model_name
            }
            collected_panel_data['action_objects'].append(data)

        if self.list_box_view is True:
            collected_panel_data['list_box_view'] = True

        return collected_panel_data
