# Django Import:
from django.urls import path

# Application Import:
from .views.test import *

app_name = 'device'

urlpatterns = [
    path('device-list/', DeviceListView.as_view(), name='list'),
    path('device-create/', TestCreateView.as_view(), name='create'),
    path('device-detail/<str:pk>', DeviceDetailView.as_view(), name='detail'),
    path('device-delete/<str:pk>', DeviceDeleteView.as_view(), name='delete'),
    path('device-update/<str:pk>', DeviceUpdateView.as_view(), name='update'),
]