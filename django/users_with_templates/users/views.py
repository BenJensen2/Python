from django.shortcuts import render, HttpResponse,redirect
from .models import *

def index(request):
    print('Server Works')
    return HttpResponse('This is the start')

def users(request):
    context = {
        "all_users" : User.objects.all()   
    }
    return render(request, 'index.html',context)

def new_user(request):
    print('New_User')
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        age = request.POST['age'],
    )
    return redirect('/users')