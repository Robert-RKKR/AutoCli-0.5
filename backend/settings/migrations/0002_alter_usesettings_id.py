# Generated by Django 4.0.2 on 2022-02-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usesettings',
            name='id',
            field=models.CharField(default='1hp3d-qw238-lfebf-pi2du-rnlt1-0sx7i', editable=False, max_length=35, primary_key=True, serialize=False),
        ),
    ]