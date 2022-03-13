# Django Import:
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin

# Admin URL pattern:
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Application URLs patterns:
urlpatterns += i18n_patterns (
    path('inventory/device/', include('inventory.urls.device_url')),
    prefix_default_language=True,
)
