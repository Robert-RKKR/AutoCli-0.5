# Django language import:
from django.utils.translation import gettext_lazy as _

# Django Import:
from django.db import models

# Managers Import:
from .managers import ActiveManager
from .managers import NotDeleted


# Validators Import:
from .validators import DescriptionValueValidator
from .validators import NameValueValidator


# Base models class:
class BaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = _('Model')
        verbose_name_plural = _('Models')

        # Permission values:
        default_permissions = ['read_only', 'read_write']
        permissions = []

        # Abstract class value:
        abstract = True

    # Model data time information:
    created = models.DateTimeField(
        verbose_name=_('Created'),
        help_text=_('Object create date.'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_('Object last update date.'),
        auto_now=True
    )

    # Model status values:
    deleted = models.BooleanField(default=False)
    root = models.BooleanField(
        verbose_name=_('Root'),
        help_text=_('Root object is not deletable.'),
        default=False
    )
    active = models.BooleanField(
        verbose_name=_('Active'),
        help_text=_(f'Status of {Meta.verbose_name} object.'),
        default=True
    )

    # Model objects manager:
    objects = NotDeleted()

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} created {self.created}'

    # Override default Delete method:
    def delete(self):
        """
            Override the default Delete method to see if the device was created by the Root user,
            if true don't change anything, otherwise change deleted value to true.
        """
        # Check if root value is True:
        if self.root == True:
            # Inform the user that the object cannot be deleted because is a root object:
            assert self.pk is not None, (
                f"{self._meta.verbose_name} object can't be deleted because its a root object.")
        else:
            # Change deleted value to True, to inform that object is deleted:
            self.deleted = True
            self.save()


class BaseMainModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Model')
        verbose_name_plural = _('Models')

        # Permission values:
        default_permissions = ['read_only', 'read_write']
        permissions = []

        # Abstract class value:
        abstract = True

    # Model validators:
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()

    # Main model values:
    name = models.CharField(
        max_length=32,
        blank=False,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'unique': f'{Meta.verbose_name} with this name already exists.',
            'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.',
        },
    )
    description = models.CharField(
        max_length=256, default=f'{Meta.verbose_name} description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
    )

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"


class BaseSubModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Model')
        verbose_name_plural = _('Models')

        # Permission values:
        default_permissions = ['read_only', 'read_write']
        permissions = []

        # Abstract class value:
        abstract = True
