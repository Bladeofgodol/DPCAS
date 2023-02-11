from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import patient
from .forms import RegistrationForm, PatientSignInForm
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
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            patient = authenticate(email=email, password=raw_password)
            login(request, patient)
            return redirect('psignup')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'psignup.html', context)


def signin(request):
    return render(request, 'asignin.html')


def psignin(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('pview')
    
    if request.POST:
        form = PatientSignInForm(request.POST)
        if form.is_valid():
            phone_number = request.POST['phone_number']
            password = request.POST['password']
            user = authenticate(phone_number=phone_number, password=password)

            if user:
                login(request, user)
                return redirect('pview')
    else:
        form = PatientSignInForm()

    context['login_form'] = form
    return render(request, 'psignin.html', context)


def plogout(request):
    logout(request)
    return redirect('psignin')
