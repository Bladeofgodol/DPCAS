from django import forms
from adminstration.models import patient, administrator,doctor
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .widgets import DatePickerInput


class DocRegForm(UserCreationForm):
	email           = forms.EmailField(max_length=60,min_length=0, help_text= "the users email")
	phone_regex     = RegexValidator(regex=r'^\+?0?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number    = forms.CharField( validators=[phone_regex], max_length=17, help_text="patient's phone number")
	date_of_birth   = forms.DateField(widget=DatePickerInput)
    
	class Meta:
		model = doctor
		fields = ("fname", "lname","phone_number", "email", "date_of_birth","password1", "password2")

	
class RegistrationForm(UserCreationForm):
    email           = forms.EmailField(max_length=60,min_length=0, help_text= "the users email")
    phone_regex     = RegexValidator(regex=r'^\+?0?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number    = forms.CharField( validators=[phone_regex], max_length=17, help_text="patient's phone number")
    date_of_birth   = forms.DateField(widget=DatePickerInput)
    
    class Meta:
        model = patient
        fields = ("fname", "lname","phone_number", "email", "date_of_birth","password1", "password2")


class PatientSignInForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    phone_regex     = RegexValidator(regex=r'^\+?0?\d{9,15}$', message="Phone number must be enterdsfsafed in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number    = forms.CharField( validators=[phone_regex], max_length=17, help_text="patient's phone number")
    
    class Meta:
        model = patient
        fields = ('phone_number', 'password')

    def clean(self):
        if self.is_valid():
            phone_number = self.cleaned_data['phone_number']
            password = self.cleaned_data['password']
            if not authenticate(phone_number = phone_number, password = password):
                raise forms.ValidationError("incorrect phone number or password")
        else:
            raise forms.ValidationError("incorrect credential format")
        

class adminSignInForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = administrator
        fields = ('email', 'password')

        def clean(self):
            if self.is_valid():

                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email = email, password = password):
                    raise forms.ValidationError("invalid login information")
                
            else:
                raise forms.ValidationError("incorrect credential format")
