# Django Import:
from django.urls import path

# Application Import:
from .views.log_view import test

urlpatterns = [
    path('test/', test, name='test'),
]