# Django Import:
from django.urls import re_path
from django.urls import path

# Application Import:
from .views.test import DeviceListView, TestCreateView, DeviceDetailView, ColorListView

app_name = 'device'

urlpatterns = [
    path('device-list/', DeviceListView.as_view(), name='list'),
    path('device-detail/<str:pk>', DeviceDetailView.as_view(), name='detail'),
    path('device-create/', TestCreateView.as_view(), name='create'),
]