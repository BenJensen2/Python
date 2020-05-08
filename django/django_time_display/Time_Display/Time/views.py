from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
    
def time(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
    }
    return render(request,'index.html', context)

def index(request):
    return HttpResponse('Index is working')

def DonkeyCheck(request):
    # return HttpResponse("That'll do donkey..... that'll do.")
    return render(request, 'shrek.html')

# Create your views here.
