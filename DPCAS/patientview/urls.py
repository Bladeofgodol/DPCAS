from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='pview'),
    path('appointment/',views.appointment, name = 'appointment'),
]