from django.shortcuts import render, HttpResponse

def index(request): #request always needs to be within function ()
    return HttpResponse("This is the start")

