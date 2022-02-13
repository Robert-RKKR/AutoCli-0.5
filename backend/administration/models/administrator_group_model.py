# Django language import:
from django.utils.translation import gettext_lazy as _

# Django Import:
from django.contrib.auth.models import Group

# Base Model Import:
from autocli.basemodel.basemodel import BaseMainModel


class AdministratorGroup(Group, BaseMainModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

    pass
