from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='admin-index'),
    path('pman/',views.pman, name='pman'),
    path('dman/',views.dman, name='dman'),
    path('psignup/', views.psignup, name='psignup'),
    path('asignin/',views.signin,name='admin-signin'),
    path('psignin/', views. psignin, name='psignin'),
    path('plogout/', views.plogout, name='plogout'),
    path('plist/',views.plist,name='plist')
]
