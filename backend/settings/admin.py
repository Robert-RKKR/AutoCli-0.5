# Django Import:
from django.contrib import admin

# Models Imports:
from .models.user_settings_model import UseSettings


# Admin classes:
@admin.register(UseSettings)
class LogAdmin(admin.ModelAdmin):

    empty_value_display = '-None-'
    list_display = (
        'pk', 'user',
    )
