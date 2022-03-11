# Django Import:
from django.urls import re_path
from django.urls import path

# Application Import:
from .views.test import DeviceListView, TestCreateView, DeviceDetailView, ColorListView

urlpatterns = [
    path('device-list/', DeviceListView.as_view(), name='device-list'),
    path('device-detail/<str:pk>', DeviceDetailView.as_view(), name='device-detail'),
    path('device-create/', TestCreateView.as_view(), name='device-create'),

    path('color-list/', ColorListView.as_view(), name='color-list'),
]