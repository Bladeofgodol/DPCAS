# Generated by Django 4.1.6 on 2023-02-12 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(help_text="patient's first name", max_length=20, verbose_name='first name')),
                ('lname', models.CharField(help_text="patient's last name", max_length=20, verbose_name='last name')),
                ('username', models.CharField(blank=True, help_text="patient's user name", max_length=50, verbose_name='username')),
                ('phone_number', models.CharField(help_text="patient's phone number", max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone number')),
                ('email', models.EmailField(blank=True, help_text="patient's email", max_length=254, unique=True, verbose_name='email')),
                ('date_of_birth', models.DateField(verbose_name='date of birth')),
                ('date_registered', models.DateField(auto_now_add=True, verbose_name='date registered')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('password', models.CharField(max_length=100, null='false', verbose_name='password')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]