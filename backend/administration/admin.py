# Django Import:
from django.contrib import admin

# Models Import:
from .models.administrator_model import Administrator
from .models.administrator_group_model import Group
from .models.settings_model import Settings


# Admins views:
admin.site.register(Administrator)
admin.site.register(Settings)
#admin.site.register(Group)