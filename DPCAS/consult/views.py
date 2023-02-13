from django.shortcuts import render


def consult (request):
    return render (request,'consult.html')

def sessions (request,chat_id):
    return render (request,'session.html',{"chat_id":chat_id})
# Create your views here.
