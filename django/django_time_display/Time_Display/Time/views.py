from django.shortcuts import render, redirect, HttpResponse
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

def GetPost(request):
    # return HttpResponse('GetPost Works')
    return render(request, 'get_post_template.html')

        # if request.method == "POST":
        #     val_from_field_one = request.POST["one"]
    	# val_from_field_two = request.POST["two"]

    # if request.method == "GET":
    #     print("a GET request is being made to this route")
    #     # return render(request, "get_post_template.html")
    # if request.method == "POST":
    #     print("a POST request is being made to this route")
    #     # return redirect("/Time/GetPost")
