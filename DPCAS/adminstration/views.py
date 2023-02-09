from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from.forms import RegistrationForm
# Create your views here.
def home(request):
    return render(request, 'adminhome.html')

def pman(request):
    return render(request, 'pman.html')

def dman(request):
    return render(request, 'dman.html')

def psignup(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            patient = authenticate(email = email,password = raw_password)
            login(request, patient)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request,'psignup.html',context)