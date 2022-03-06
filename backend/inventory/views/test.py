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
from logger.logger import Logger


class TestClass(ListView):

    panel = None
    
    # GET request response page:
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = self.get_context_data()
        context['panel'] = self.panel
        return self.render_to_response(context)

class AddForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ('active', 'name', 'hostname')


class TestListView(TestClass):

    model = Device
    template_name = 'base_views/list_view.html'
    paginate_by = 5
    panel = ['RKKR']


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
