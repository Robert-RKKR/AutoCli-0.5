# Django Import:
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

# Models Imports:
from .models.credential_model import Credential
from .models.device_model import Device
from .models.folde_model import Folder
from .models.color_model import Color

# Admin classes:
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):

    empty_value_display = '-None-'
    list_display = (
        'pk', 'name', 'root_folder', 'credential',
    )
    search_fields = (
        'name',
    )
    fieldsets = (
        (_('Status'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('active',)
        }),
        (_('Basic settings'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', 'root_folder', 'description')
        }),
        (_('Relationships with other models'), {
            'classes': ('collapse',),
            'fields': ('devices',),
        }),
        (_('Defaults main values'), {
            'classes': ('collapse',),
            'fields': ('ico', 'ssh_port', 'https_port'),
        }),
        (_('Defaults security and credentials'), {
            'classes': ('collapse',),
            'fields': ('credential', 'secret', 'certificate'),
        }),
    )


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):

    empty_value_display = '-None-'
    list_display = (
        'pk', 'name', 'hostname', 'active', 'ssh_status', 'https_status',
    )
    list_filter = (
        'device_type', 'ssh_status', 'https_status', 'certificate',
    )
    search_fields = (
        'name', 'hostname',
    )
    ordering = (
        'name',
    )
    fieldsets = (
        (_('Status'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('active',)
        }),
        (_('Basic settings'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', 'hostname', 'description')
        }),
        (_('Additional settings'), {
            'classes': ('collapse',),
            'fields': ('device_type', 'ico', 'ssh_port', 'https_port',),
        }),
        (_('Security and credentials'), {
            'classes': ('collapse',),
            'fields': ('credential', 'secret', 'token', 'certificate',),
        }),
    )

# Register Application models in Django Admin:
admin.site.register(Color)
admin.site.register(Credential)
# admin.site.register(DeviceType)
# admin.site.register(DeviceData)
# admin.site.register(DeviceRawData)
# admin.site.register(DeviceInterface)
