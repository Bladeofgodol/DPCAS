from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dsignin/', views.dsignin, name='dsignin'),
    path('psignin/', views.psignin, name='psignin'),
]


