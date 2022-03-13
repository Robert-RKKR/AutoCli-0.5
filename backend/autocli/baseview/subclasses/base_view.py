# Python Import:
import re

# Django Import:
from django.views import View


# Create View class:
class BaseView(View):

    singular_panel = None
    plural_panel = None
    list_box_view = None

    def get(self, request, *args, **kwargs):
        """ Overwrite get function. """

        # Inherit functionality from get function:
        super().get(request, *args, **kwargs)
        # Collect context data:
        context = self.get_context_data()
    
        # Return HTML response:
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        """ Overwrite post function. """

        # Inherit functionality from get function:
        super().get(request, *args, **kwargs)
        # Collect context data:
        context = self.get_context_data()

        # Return HTML response:
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """ Overwrite get_context_data function. """

        # Inherit functionality from get_context_data function:
        context = super().get_context_data(**kwargs)

        ### Collect and send data to HTML template ###

        # Add panel data to HTML template:
        context['panel'] = self._collect_panel_data()
        # Submit current URL request to HTML template:
        url = self.request.build_absolute_uri()
        context['current_url'] = url
        # Submit carrent URL with out display request to HTML template:
        context['current_url_no_display'] = self._no_display_url(url)
        # Submit display_version value to HTML template:
        context['display_version'] = self._chaeck_display_version(url)
        # Submit class name to HTML template:
        class_name = self._collect_class_name()
        context['class_name'] = class_name
        # Submit links to HTML template:
        context['detail_link'] = class_name + ':detail'
        context['create_link'] = class_name + ':create'
        context['delete_link'] = class_name + ':delete'
        context['update_link'] = class_name + ':update'

        # Return context data:
        return context

    def _collect_class_name(self):
        return self.model._meta.object_name.lower()

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
            'singular_panel': False,
            'plural_panel': False,
            'list_box_view': False
        }

        if self.list_box_view is True:
            collected_panel_data['list_box_view'] = True

        if self.singular_panel is True:
            collected_panel_data['singular_panel'] = True
            return collected_panel_data
        elif self.plural_panel is True:
            collected_panel_data['plural_panel'] = True
            return collected_panel_data
        else:
            return collected_panel_data
