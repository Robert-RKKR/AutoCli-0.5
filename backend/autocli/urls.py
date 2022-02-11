# Django Import:
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    # Applications URL-s:
    path('logger/', include('logger.urls')),
]
