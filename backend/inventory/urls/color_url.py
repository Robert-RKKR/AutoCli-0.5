# Django Import:
from django.urls import path

# Application Import:
from ..views.color_view import *

app_name = 'color'

urlpatterns = [
    path('list/', ModelListView.as_view(), name='list'),
    path('create/', ModelCreateView.as_view(), name='create'),
    path('detail/<str:pk>', ModelDetailView.as_view(), name='detail'),
    path('delete/<str:pk>', ModelDeleteView.as_view(), name='delete'),
    path('update/<str:pk>', ModelUpdateView.as_view(), name='update'),
]
