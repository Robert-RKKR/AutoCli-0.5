# Django Import:
from django.contrib import admin

# Models Imports:
from logger.models.log_details_model import LogDetails
from logger.models.log_model import Log


# Admins views:
admin.site.register(LogDetails)
admin.site.register(Log)
