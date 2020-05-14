from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
unique_id = get_random_string(length=32)

def index(request):
    # context = {
    #     'count' : 0
    # }
    return HttpResponse('It Works!!')

def random_word(request):
    word = get_random_string(length=14)
    count = request.session['count']
    request.session['count'] = count+1
    print(request.session['count'])
    # context['count']=context['count']+1
    context = {
        'word' : word,
        'count' : request.session['count']
    }
    return render(request,'index.html',context)

def reset(request):
    request.session['count'] = 0
    return redirect('/random_word')