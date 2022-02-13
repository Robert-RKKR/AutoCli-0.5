# Django language import:
from django.utils.translation import gettext_lazy as _

# Django Import:
from django.contrib import admin

# Models Import:
from .models.administrator_model import Administrator
from .models.administrator_group_model import Group
from .models.settings_model import Settings


# Admins views:
admin.site.register(Settings)
#admin.site.register(Group)


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):

    empty_value_display = '-None-'
    list_display = (
        'username', 'first_name', 'last_name', 'admin', 'superuser',
    )
    list_filter = (
        'groups', 'admin', 'superuser',
    )
    search_fields = (
        'username', 'first_name', 'last_name',
    )
    ordering = (
        'username',
    )
    fieldsets = (
        (_('Basic administrator information'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('username', 'email')
        }),
        (_('Administrator access'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('admin', 'staff', 'superuser', 'groups'),
        }),
        (_('Administrator personal details'), {
            'classes': ('collapse',),
            'fields': ('first_name', 'middle_name', 'last_name'),
        }),
    )
