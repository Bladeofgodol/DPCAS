from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'ppage.html')


def appointment(request):
    return render(request, 'appointment.html')

