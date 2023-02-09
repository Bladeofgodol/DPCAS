# Generated by Django 4.1.6 on 2023-02-09 05:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(help_text="patient's first name", max_length=20, verbose_name='first name')),
                ('lname', models.CharField(help_text="patient's last name", max_length=20, verbose_name='last name')),
                ('username', models.CharField(blank=True, help_text="patient's user name", max_length=50, unique=True, verbose_name='username')),
                ('pno', phonenumber_field.modelfields.PhoneNumberField(help_text="patient's phone number", max_length=128, region=None, unique=True, verbose_name='phone number')),
                ('email', models.EmailField(blank=True, help_text="patient's email", max_length=254, unique=True, verbose_name='email')),
                ('date_of_birth', models.DateField(verbose_name='date of birth')),
                ('date_registered', models.DateField(auto_now_add=True, verbose_name='date registered')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('password', models.CharField(max_length=50, null='false', verbose_name='password')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
