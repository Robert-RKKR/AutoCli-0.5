# Django language import:
from django.utils.translation import gettext_lazy as _
from django.db import IntegrityError

# Django Import:
from django.db import models
import random
import string

# Managers Import:
from .managers import ActiveManager
from .managers import NotDeleted


# Validators Import:
from .validators import DescriptionValueValidator
from .validators import NameValueValidator


def primary_key_generator():
    """ Generate primary key. """

    # Create template string: 
    template_string = string.ascii_lowercase + string.digits

    # Primary key:
    primary_key = ''

    # primary key generator:
    for row in range(1, 31):
        if row % 5 == 0:
            if row != 30:
                primary_key = primary_key + random.choice(template_string) + '-'
            else:
                primary_key = primary_key + random.choice(template_string)
        else:
            primary_key = primary_key + random.choice(template_string)

    # Return generated primary key:
    return primary_key


# Base models class:
class BaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = _('Model')
        verbose_name_plural = _('Models')

        # Abstract class value:
        abstract = True

    # Model validators:
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()

    # Model ID:
    id = models.CharField(
        primary_key=True,
        max_length=35,
        editable=False,
    )

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

    # Main model values:
    name = models.CharField(
        verbose_name=_('Name'),
        help_text=_('Xxx.'),
        max_length=32,
        blank=False,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'unique': 'Object with this name already exists.',
            'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.',
        },
    )
    description = models.CharField(
        verbose_name=_('Description'),
        help_text=_('Xxx.'),
        max_length=256, default=f'{Meta.verbose_name} description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
    )

    # Model objects manager:
    objects = NotDeleted()

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} created {self.name}'

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

    # Override default Sace method:
    def save(self, *args, **kwargs):
        if not self.id:
            self.pk = primary_key_generator()

        success = False
        failures = 0
        while not success:
            try:
                super(BaseModel, self).save(*args, **kwargs)
            except IntegrityError:
                failures += 1
                if failures > 5:
                    # Raise error in case of fails of quintuple save proccess:
                    raise('Object save make a problem.')
                else:
                    # In case of auto-generate key duplication, regenerate key value:
                    self.id = primary_key_generator()
            else:
                # Mark save process success:
                 success = True

        # Return success value:
        return success
