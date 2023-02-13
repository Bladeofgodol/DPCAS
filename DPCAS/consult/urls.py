from django.urls import path
from . import views

urlpatterns = [
    path('',views.consult,name='consult'),
    path('session/<str:chat_id>/',views.sessions, name='session'),
]