# Python Import:
import re

# Django Imports:
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import View, ListView
from django.shortcuts import render
from django import forms

# Models Imports:
from logger.models.log_details_model import LogDetails
from logger.models.log_model import Log

# Application Import:
from inventory.models.device_model import Device
from inventory.filters.device_filter import DeviceFilter
from logger.logger import Logger


class TestClass(ListView):

    panel = None
    singular_panel = None
    plural_panel = None
    filterset = None

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
        super().get(request, *args, **kwargs)
        context = self.get_context_data()
        context['panel'] = self._collect_panel_data()
        return self.render_to_response(context)

    def _collect_panel_data(self):
        collected_panel_data = []
        model_name = self.model._meta.object_name.lower() + '-create'

        if self.plural_panel is True:
            data = {
                'ico': 'create',
                'link': model_name
            }
            collected_panel_data.append(data)

        return collected_panel_data

class AddForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ('active', 'name', 'hostname')


class DeviceListView(TestClass):

    model = Device
    template_name = 'base_views/list_view.html'
    paginate_by = 5
    filterset = DeviceFilter
    plural_panel = True


class DeviceDetailView(DetailView):

    model = Device
    template_name = 'base_views/detail_view.html'


class TestCreateView(CreateView):
    template_name = 'add.html'
    model = Device
    form_class = AddForm
    success_url = '/'


class Test(View, PermissionRequiredMixin):

    permission_required = 'log.read_write'

    def get(self, request, *args, **kwargs):

        data = {
            'output': 'RKKR',
            'page_name': 'RKKR - Test view'
        }

        lagdata = {
            'Test1': 'RKKR 1',
            'Test2': 'RKKR 2'
        }

        logger = Logger('Test', False)
        logger.error('Test log', **lagdata)

        data['logs'] = Log.objects.all()

        # Return valid page with provided or default data:
        return render(request, 'test.html', data)
