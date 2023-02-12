from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='admin-index'),
    path('pman/',views.pman, name='pman'),
    path('dman/',views.dman, name='dman'),
    path('psignup/', views.psignup, name='psignup'),
    path('psignin/', views. psignin, name='psignin'),
    path('plogout/', views.plogout, name='plogout'),
    path('alogin/',views.adminlogin,name='alogin'),
    path('plist/',views.plist,name='plist'),
    path('alogout/',views.alogout, name='alogout'),
    path('dsignup/',views.dsignup, name='dsignup'),
    path('dlist/',views.dlist,name='dlist'),
]
