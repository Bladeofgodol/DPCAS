from django.contrib import admin
from adminstration.models import patient, administrator,doctor
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ( 'fname','lname','phone_number','last_login','username','date_registered','email','is_active')
    search_fields = ( 'phone_number','email','fname','lname')
    readonly_fields = ('date_registered','last_login','date_of_birth')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(patient,AccountAdmin)

class AccountAdministrators(UserAdmin):
    list_display = ( 'fname','lname','last_login','username','date_registered','email','is_active','is_staff')
    search_fields = ( 'phone_number','email','fname','lname')
    readonly_fields = ('date_registered','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(administrator,AccountAdministrators)


class Doctorsadmin(UserAdmin):
    list_display = ( 'fname','lname','last_login','username','date_registered','email','is_active','is_staff')
    search_fields = ( 'phone_number','email','fname','lname')
    readonly_fields = ('date_registered','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(doctor,Doctorsadmin)
