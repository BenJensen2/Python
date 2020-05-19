from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import UserManager, User
import datetime
import bcrypt

def index(request):
    request.session.flush()
    return render(request,'user.html')

def create(request):
    # print(request,"Request")
    today = datetime.date.today()
    # "2020-05-19"
    birthday = request.POST['bday']
    birthday_year = int(birthday[0:4])
    birthday_month = int(birthday[5:7])
    birthday_day = int(birthday[8:9])

    if today.year-13 > birthday_year:
        if today.month > birthday_month:
            if today.day > birthday_day:
                print('User is at least 13 years old!')
            
    else:
        print('User is not 13 years old')

    print(today)
    print(birthday_year)
    print(birthday_month)
    print(birthday_day)
    # if today.year-13 > birthday.year:
    #     print('more than 13 years')
    # else:
    #     print('User is younger than 13 years old')

    # print(today)
    # print(today.year-13)
    # print(today.month)
    # print(today.day)



    print(request.POST['fname'])
    print(request.POST['lname'])
    print(request.POST['bday'])
    print(request.POST['email'])
    print(request.POST['pword'])
    print(request.POST['pword_confirm'])
    
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
                        # messages.error(request,value, extra_tags=key)
            # This is overwriting each error every time
            # Need to create a dictionary that html loops over
        return redirect('/')
    else:

        password_encoded = bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'], 
            birthday = request.POST['bday'],
            email_address = request.POST['email'],
            password = password_encoded,
        )
        request.session['user_email'] = request.POST['email']
        # request.session['pword'] = User.password
        request.session['fname'] = request.POST['fname']

        # Name validations
        # Compare email to see if already in use
        # Compare passwords, only create one
        # Show errors
        # if all correct: redirect to success
        return redirect('/success')

def login(request):
    # print('Login Linked')
    # print(request.POST['email'])
    # print(request.POST['pword'])
    users = User.objects.all()
    print(users)
    user_exist = False
    for user in users:
        if request.POST['email'] == user.email_address:
            if bcrypt.checkpw(request.POST['pword'].encode(),user.password.encode()):
                request.session['user_email'] = user.email_address
                # request.session['pword'] = user.password
                print(user.email_address)
                print(user.password)
                user_exist = True
    if user_exist == False:
        print('Email/Password is incorrect or User does not exist')
    # Show errors
    # If correct, login: redirect to success
    return redirect('/success')

def success(request):
    if 'user_email' in request.session:
        print('Username and Password in session')
        # first_name = "Jonny"
        #request.session['fname']
        context = {
            'first_name' : User.objects.get(email_address=request.session['user_email']).first_name
        }
        return render(request,'success.html',context)
    else:
        return HttpResponse('You do not have access to this site.  Login to proceed')
    # return HttpResponse(f'Awesome job again my good and faithful son {first_name}')


# Transparency