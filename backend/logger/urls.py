# Django Import:
from django.urls import path

# Application Import:
from .views.log_view import Test

urlpatterns = [
    path('test/', Test.as_view(), name='test'),
]