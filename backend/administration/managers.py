# Django Import:
from django.contrib.auth.models import BaseUserManager
from django.apps import apps

# Application Import:
from .models.settings_model import Settings


class AdministratorManager(BaseUserManager):

    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):

        # Check if basic values are avaliable:
        if not username:
            raise ValueError('Administrator must have an username value.')
        if not password:
            raise ValueError('Administrator must have a password value.')

        # Propose username in user creation process:
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)

        # Verify collected data about new administrator:
        if email is None:
            new_administrator = self.model(
                username=username,
            )
        else:
            email = self.normalize_email(email)
            new_administrator = self.model(
                username=username,
                email=email,
            )
        new_administrator.active = is_active
        new_administrator.staff = is_staff
        new_administrator.superuser = is_superuser
        new_administrator.set_password(password)
        new_administrator.save(using=self._db)

        # Create user application settings:
        user_settings = Settings.objects.create(administrator=new_administrator)

        return new_administrator

    def create_user(self, username, password, email=None, **extra_fields):
        return self._create_user(
            username=username,
            email=email,
            password=password,
            is_active=True,
            is_staff=False,
            is_superuser=False,
            extra_fields=extra_fields,
        )

    def create_superuser(self, username, password, email=None, **extra_fields):
        return self._create_user(
            username=username,
            email=email,
            password=password,
            is_active=True,
            is_staff=True,
            is_superuser=True,
            extra_fields=extra_fields,
        )

    class Meta:
        default_permissions = ['read_only', 'read_write']
        permissions = []
