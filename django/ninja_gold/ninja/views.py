from django.shortcuts import render, HttpResponse


def index(request):
    # return HttpResponse("Index Works!!")
    return render(request, 'index.html')

def process_money(request):
    request.session['your_gold']=10
    # return HttpResponse('Process Money Worked')
    if request.method == "POST":
        # print(request.POST['gold'])
        if request.POST['gold']=='farm':
            gold = gold+10
            print(f'The Farm is Here!! {gold}')
    return render(request, 'index.html')
        # return HttpResponse('Farm Posted')
        # if request.POST["name"] == 'farm_gold':
        #     return HttpResponse('Farm Gold!!')

# Create your views here.
