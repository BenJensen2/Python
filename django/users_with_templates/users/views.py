from django.shortcuts import render, HttpResponse,redirect
from .models import *

def index(request):
    print('Server Works')
    return HttpResponse('This is the start')

def users(request):
    # print('Users Page')
    for identity in User.objects.all():
        # context = {
            
        # }
        print(identity.first_name)
    # print(User.objects.get(id=1).first_name)
    # for people in User.objects.all()
    #     print(User.objects['first_name')
    return render(request, 'index.html')

def new_user(request):
    print('New_User')
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        age = request.POST['age'],
    )

    # fname = request.POST['first_name']
    # lname = request.POST['last_name']
    # mail = request.POST['email']
    # old = request.POST['age']

    # print(fname)
    # print(lname)
    # print(mail)
    # print(old)

    return redirect('/users')