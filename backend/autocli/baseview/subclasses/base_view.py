# Python Import:
import re

# Django Import:
from django.views import View


# Create View class:
class BaseView(View):

    singular_panel = None
    plural_panel = None
    list_box_view = None

    def _chaeck_display_version(self, url):
        """ Check display version based on provided URL or default value. """

        ### Collect display version from URL:
        version = None
        # Collect current display value from session:
        session_version = self.request.session.get('display_version', None)
        # Search URL to find all query values:
        query_values = re.findall(r'(\w*=\w{1,})', url)
        # Collect display value from all query values:
        for row in query_values:
            if 'display' in row:
                try:
                    version = int(row.split('=')[1])
                except:
                    version = 1

        # If display value collected from session is None,
        # use provided in URL or default if not provided:
        if session_version is None:
            if version is None:
                version = 1
            self.request.session['display_version'] = version
        # If display value is provided by session,
        # check if value is tha same like value provided by URL.
        # Value provided by URL overides value collected from session:
        else:
            if version is None:
                version = session_version
            elif session_version != version:
                self.request.session['display_version'] = version

        # Return default value:
        return version

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
