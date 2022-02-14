# Generated by Django 4.0.2 on 2022-02-14 10:23

import autocli.basemodel.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UseSettings',
            fields=[
                ('id', models.CharField(default='orv7a-4jc72-8pjw0-h873x-25580-99j6t', editable=False, max_length=35, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Object create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Object last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False)),
                ('root', models.BooleanField(default=False, help_text='Root object is not deletable.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Status of Model object.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Model with this name already exists.'}, max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()])),
                ('description', models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()])),
                ('default_connection_username', models.CharField(default='admin', help_text='Default SSH/HTTPS connection username.', max_length=64, verbose_name='Default username.')),
                ('default_connection_password', models.CharField(default='password', help_text='Default SSH/HTTPS connection password.', max_length=64, verbose_name='Default password.')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User settings',
                'verbose_name_plural': 'Users settings',
            },
        ),
    ]
