# Django language import:
from django.utils.translation import gettext_lazy as _

# Django Import:
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Validators Import:
from ..validators import UsernameValueValidator
from ..validators import PasswordValueValidator
from ..validators import NameValueValidator

# Application Import:
from ..managers import AdministratorManager

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel
from .administrator_group_model import Group


class Administrator(BaseModel, AbstractBaseUser, PermissionsMixin):

    class Meta:
        
        # Model name values:
        verbose_name = _('Administrator')
        verbose_name_plural = _('Administrators')

    # Model validators:
    username_validator = UsernameValueValidator()
    password_validator = PasswordValueValidator()
    name_validator = NameValueValidator()

    # Last login value:
    last_login = models.DateTimeField(blank=True, null=True)

    # Django related model values:
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    # Group model corelation:
    groups = models.ManyToManyField(Group, blank=True)

    # Basic model valuse:
    username = models.CharField(
        verbose_name=_('Username'),
        help_text=_('Administrator username.'),
        max_length=32,
        unique=True,
        validators=[username_validator],
        error_messages={
            'null': _('Username field is mandatory.'),
            'blank': _('Username field is mandatory.'),
            'unique': _('Administrator with this username already exists.'),
            'invalid': _('Enter the correct username value. It must contain 4 to 32 digits, letters and spaces.'),
        },
    )
    password = models.CharField(
        verbose_name=_('Password'),
        help_text=_('Administrator password.'),
        max_length=128,
        validators=[password_validator],
        error_messages={
            'null': _('Password field is mandatory.'),
            'blank': _('Password field is mandatory.'),
            'invalid': _('Enter the correct password value. It requires at least one lowercase letter, one uppercase letter, one digit and one special character (@$!%*?&), minimum 8 characters.'),
        },
    )
    email = models.EmailField(
        verbose_name=_('E-mail'),
        help_text=_('Administrator e-mail address.'),
        max_length=128,
        unique=True,
        blank=True,
        null=True,
        error_messages={
            'unique': _('Administrator with this e-mail already exists.'),
            'invalid': _('Enter the correct e-mail value.'),
        },
    )

    # Personal values:
    first_name = models.CharField(
        verbose_name=_('First name'),
        help_text=_('Administrator first name.'),
        max_length=32,
        blank=True,
        null=True,
        validators=[name_validator],
        error_messages={
            'null': _('First name field is mandatory.'),
            'blank': _('First name field is mandatory.'),
            'unique': _('First name with this name already exists.'),
            'invalid': _('Enter the correct first name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.'),
        },
    )
    middle_name = models.CharField(
        verbose_name=_('Middle name'),
        help_text=_('Administrator middle name.'),
        max_length=32,
        blank=True,
        null=True,
        validators=[name_validator],
        error_messages={
            'null': _('Middle name field is mandatory.'),
            'blank': _('Middle name field is mandatory.'),
            'unique': _('Middle name with this name already exists.'),
            'invalid': _('Enter the correct middle name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.'),
        },
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        help_text=_('Administrator last name.'),
        max_length=32,
        blank=True,
        null=True,
        validators=[name_validator],
        error_messages={
            'null': _('Last name field is mandatory.'),
            'blank': _('Last name field is mandatory.'),
            'unique': _('Last name with this name already exists.'),
            'invalid': _('Enter the correct last name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.'),
        },
    )

    # User Constants:
    USERNAME_FIELD = 'username'

    # User Manager:
    objects = AdministratorManager()

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.username}"

    # Model methods:
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username

    # Model property:
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.superuser
