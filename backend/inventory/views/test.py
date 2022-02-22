# Django Imports:
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.shortcuts import render
from django import forms

# Models Imports:
from logger.models.log_details_model import LogDetails
from logger.models.log_model import Log

# Application Import:
from inventory.models.device_model import Device
from logger.logger import Logger

from autocli.baseview.views.list_view import ListView


class AddForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ('active', 'name', 'hostname')


class TestListView(ListView):

    model = Device
    paginate_by = 2
    filter_by = ['name', 'hostname']
    queryset = Device.objects.filter(active=True).order_by('name')


class TestCreateView(CreateView):
    template_name = 'add.html'
    model = Device
    form_class = AddForm
    success_url = '/add/'


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
