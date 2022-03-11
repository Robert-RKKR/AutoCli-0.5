# Django language import:
from django.utils.translation import gettext_lazy as _

# Django Import:
from django.contrib.auth.models import User
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel


class UseSettings(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('User settings')
        verbose_name_plural = _('Users settings')

    # Administrator:
    user = models.OneToOneField(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
    )

    # User application settings:
    default_connection_username = models.CharField(
        verbose_name=_('Default username.'),
        help_text=_('Default SSH/HTTPS connection username.'),
        max_length=64,
        default='admin',
    )
    default_connection_password = models.CharField(
        verbose_name=_('Default password.'),
        help_text=_('Default SSH/HTTPS connection password.'),
        max_length=64,
        default='password',
    )

    # Model representation:
    def __str__(self) -> str:
        return f"Settings({self.pk}: {self.administrator})"
