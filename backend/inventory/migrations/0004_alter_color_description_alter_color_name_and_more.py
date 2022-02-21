# Generated by Django 4.0.2 on 2022-02-21 12:57

import autocli.basemodel.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_credential_options_alter_device_options_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='description',
            field=models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Xxx.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Xxx.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='description',
            field=models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Xxx.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Xxx.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Xxx.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='device',
            name='https_status',
            field=models.BooleanField(default=False, help_text='Status of HTTPS connection to the device.', verbose_name='HTTPS status'),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Xxx.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='device',
            name='ssh_status',
            field=models.BooleanField(default=False, help_text='Status of SSH connection to the device.', verbose_name='SSH status'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='description',
            field=models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Xxx.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='devices',
            field=models.ManyToManyField(blank=True, help_text='All devices that belongs to current folder.', to='inventory.Device', verbose_name='Devices'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Xxx.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name'),
        ),
    ]