# Django Import:
from django.urls import re_path
from django.urls import path

# Application Import:
from .views.test import Test, TestListView, TestCreateView

urlpatterns = [
    path('test/', Test.as_view(), name='test'),
    path('list/', TestListView.as_view(), name='list'),
    path('add/', TestCreateView.as_view(), name='add'),
]