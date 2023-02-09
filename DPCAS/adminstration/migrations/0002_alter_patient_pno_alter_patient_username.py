# Generated by Django 4.1.6 on 2023-02-09 05:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='pno',
            field=models.CharField(help_text="patient's phone number", max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='username',
            field=models.CharField(blank=True, help_text="patient's user name", max_length=50, verbose_name='username'),
        ),
    ]