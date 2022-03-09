# Django Import:
from django.urls import re_path
from django.urls import path

# Application Import:
from .views.test import Test, DeviceListView, TestCreateView, DeviceDetailView

urlpatterns = [
    path('test/', Test.as_view(), name='test'),
    path('device-list/', DeviceListView.as_view(), name='device-list'),
    path('device-detail/<str:pk>', DeviceDetailView.as_view(), name='device-detail'),
    path('device-create/', TestCreateView.as_view(), name='device-create'),
]