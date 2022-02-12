# Django Import:
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Validators Import:
from ..validators import UsernameValueValidator
from ..validators import PasswordValueValidator

# Application Import:
from ..managers import AdministratorManager

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel
from .administrator_group_model import Group


class Administrator(BaseModel, AbstractBaseUser, PermissionsMixin):

    # Model validators:
    username_validator = UsernameValueValidator()
    password_validator = PasswordValueValidator()

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
        max_length=32,
        blank=False,
        unique=True,
        validators=[username_validator],
        error_messages={
            'null': 'Username field is mandatory.',
            'blank': 'Username field is mandatory.',
            'unique': 'Administrator with this username already exists.',
            'invalid': 'Enter the correct username value. It must contain 4 to 32 digits, letters and spaces.',
        },
    )
    password = models.CharField(
        max_length=128,
        validators=[password_validator],
        error_messages={
            'null': 'Password field is mandatory.',
            'blank': 'Password field is mandatory.',
            'invalid': 'Enter the correct password value. It requires at least one lowercase letter, one uppercase letter, one digit and one special character (@$!%*?&), minimum 8 characters.',
        },
    )
    email = models.EmailField(
        max_length=128,
        unique=True,
        blank=True,
        null=True,
        error_messages={
            'null': 'E-mail field is mandatory.',
            'blank': 'E-mail field is mandatory.',
            'unique': 'Administrator with this e-mail already exists.',
            'invalid': 'Enter the correct e-mail value.',
        },
    )

    # Personal values:
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

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
