# Generated by Django 4.0.2 on 2022-02-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_usesettings_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usesettings',
            name='id',
            field=models.CharField(default='u69xq-stlm2-g5e1r-dzofx-tvoqa-zlsoe', editable=False, max_length=35, primary_key=True, serialize=False),
        ),
    ]