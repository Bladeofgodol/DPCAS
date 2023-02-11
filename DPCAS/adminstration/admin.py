from django.contrib import admin
from adminstration.models import patient
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ( 'fname','lname','phone_number','last_login','username','date_registered','email','is_active')
    search_fields = ( 'phone_number','email','fname','lname')
    readonly_fields = ('date_registered','last_login','date_of_birth')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(patient,AccountAdmin)