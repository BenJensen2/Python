from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from .models import UserManager, User
import datetime
import bcrypt


def index(request):
    request.session.flush()
    return render(request,'login_registration.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:

        password_encoded = bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'], 
            # birthday = request.POST['bday'],
            email_address = request.POST['email'],
            password = password_encoded,
        )
        request.session['user_email'] = request.POST['email']
        request.session['fname'] = request.POST['fname']

        return redirect('/success')

def success(request):
    if 'user_email' in request.session:

        context = {
            'first_name' : request.session['fname']# User.objects.get(email_address=request.session['user_email']).first_name
        }
        return render(request,'success.html',context)
    else:
        return HttpResponse('You do not have access to this site.  Login to proceed')

def login(request):
    user = User.objects.filter(email_address=request.POST['email'])
    if user:
        if bcrypt.checkpw(request.POST['pword'].encode(), user[0].password.encode()):
            request.session['user_email'] = user[0].email_address
            request.session['fname'] = user[0].first_name
            request.session['id'] = user[0].id
            # return redirect('/success')
            return redirect('/books')

    else:
        print('Email/Password is incorrect or User does not exist')

    return redirect('/success')