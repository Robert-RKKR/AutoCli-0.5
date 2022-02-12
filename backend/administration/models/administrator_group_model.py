# Django Import:
from django.contrib.auth.models import Group

# Base Model Import:
from autocli.basemodel.basemodel import BaseMainModel


class AdministratorGroup(Group, BaseMainModel):

    pass
