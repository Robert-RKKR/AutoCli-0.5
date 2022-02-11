# Django Import:
from django.contrib import admin

# Models Imports:
from logger.models.log_details_model import LogDetails
from logger.models.log_model import Log


# Admin classes:
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):

    empty_value_display = '-None-'
    list_display = (
        'pk', 'timestamp', 'severity', 'message',
    )
    list_filter = (
        'severity',
    )
    search_fields = (
        'timestamp', 'message',
    )
    ordering = (
        'pk', 'timestamp',
    )
