from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('pman/',views.pman, name='pman'),
    path('dman/',views.dman, name='dman'),
    path('psignup/', views.psignup, name='psignup'),
]
