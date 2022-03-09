# Django Imports:
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View
from django.shortcuts import render
from django import forms

# Models Imports:
from logger.models.log_details_model import LogDetails
from logger.models.log_model import Log

# Application Import:
from inventory.models.device_model import Device
from inventory.filters.device_filter import DeviceFilter
from logger.logger import Logger

# Own views models:
from autocli.baseview.views.list_view import ListView
from autocli.baseview.views.detail_view import DetailView
from autocli.baseview.views.update_view import UpdateView
from autocli.baseview.views.delete_view import DeleteView
from autocli.baseview.views.create_view import CreateView


class AddForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ('active', 'name', 'hostname')


class DeviceListView(ListView):

    model = Device
    filterset = DeviceFilter
    plural_panel = True


class DeviceDetailView(DetailView):

    model = Device


class TestCreateView(CreateView):

    model = Device
    form_class = AddForm
