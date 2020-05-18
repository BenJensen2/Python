from django.shortcuts import render, HttpResponse,redirect
from .models import *


def index(request):
    return HttpResponse("This Works!!")

def all_ninjas(request):
    context = {"all_dojos" : dojos.objects.all()}
    return render(request, 'index.html',context)

def new_dojo(request):
    print('New_Dojo')
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    desc = "A New Dojo"
    context = {
        "name" : name,
        "city" : city,
        "state" : state,
        "desc" : desc
    }
    print(context)
    dojos.objects.create(name=name,city=city,state=state,desc=desc)
    return redirect('/ninjas')

def new_ninja(request):
    print('New_Ninja')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo_id = request.POST['dojo_id']
    context = {
        "first_name" : first_name,
        "last_name" : last_name,
        "dojo_id" : dojo_id,
    }
    print(context)

    ninjas.objects.create(first_name=first_name,last_name=last_name,dojo=dojos.objects.get(id=dojo_id))
    print(context)
    return redirect('/ninjas')

def delete_dojo(request):
    dojo_id = request.POST['dojo_id']
    print(dojo_id)
    print('Delete Dojo')
    dojos.objects.get(id=dojo_id).delete()
    return redirect('/ninjas')

def delete_ninja(request):
    ninja_id = request.POST['ninja_id']
    print(ninja_id)
    print('Delete Ninja')
    ninjas.objects.get(id=ninja_id).delete()
    return redirect('/ninjas')