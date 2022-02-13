# Django language import:
from django.utils.translation import gettext_lazy as _

# Django Import:
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseMainModel


class Settings(BaseMainModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Settings')
        verbose_name_plural = _('Settings')

    # Administrator:
    administrator = models.OneToOneField(
        'Administrator',
        on_delete=models.CASCADE,
    )

    # User application settings:
    default_connection_username = models.CharField(
        max_length=64,
        default='admin',
    )
    default_connection_password = models.CharField(
        max_length=64,
        default='password',
    )

    # Model representation:
    def __str__(self) -> str:
        return f"Settings({self.pk}: {self.administrator})"