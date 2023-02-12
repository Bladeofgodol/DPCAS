from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.contrib.auth import login, authenticate, logout
from .models import patient, administrator
from .forms import RegistrationForm, PatientSignInForm, adminSignInForm
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

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            user = form.save()
            login(request, user)

            return redirect('psignup')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'psignup.html', context)


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

            # else:
            #     return redirect('pview')
        else:
            context['login_form'] = form
    else:
        
        form = PatientSignInForm()

    context['login_form'] = form
    return render(request, 'psignin.html', context)


def plogout(request):
    logout(request)
    return redirect('psignin')


def plist(request):
    patients = patient.objects.all()
    return render(request, 'plist.html', {'patients': patients})


def adminlogin(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('admin-index')

    if request.POST:
        form = adminSignInForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
        
        

            if user:
                login(request, user)
                return redirect('admin-index')
            
        #     else:
        #         return HttpResponse('user doesnt exist')
        # else:
        #     return HttpResponse('not valid')
    else:
        
        form = adminSignInForm()

    context['login_form'] = form
    return render(request, 'asignin.html', context)


def alogout(request):
    logout(request)
    return redirect('alogin')
