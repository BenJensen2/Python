from django.shortcuts import render, HttpResponse
import random
# from jinja2 import Template
# No need to import jinja, already within django and syntax will read in html
# Append to seesions, ensure to sessions.save() then loop through jinja in html


def index(request):
    request.session['current_gold']=0 # Pass initial gold value of 0 for display
    context = {
        "current_gold": request.session['current_gold']

    }
    return render(request, 'index.html',context)

def process_money(request):
    print(request.session['current_gold'])

    if request.method == "POST":
        if request.POST['location']=='farm':
            new_gold = random.randrange(10,21,1)
            print(new_gold)
            request.session['current_gold']+= new_gold
            output = f"Earned {new_gold} golds from the {request.POST['location']}!"
            print(output)
        
        elif request.POST['location']=='cave':
            new_gold = random.randrange(5,11,1)
            print(new_gold)
            request.session['current_gold']+= new_gold
            print(request.session['current_gold'])
            output = f"Earned {new_gold} golds from the {request.POST['location']}!"
            print(output)

        elif request.POST['location']=='house':
            new_gold = random.randrange(2,6,1)
            print(new_gold)
            request.session['current_gold']+= new_gold
            print(request.session['current_gold'])
            output = f"Earned {new_gold} golds from the {request.POST['location']}!"
            print(output)

        elif request.POST['location']=='casino':
            new_gold = random.randrange(-50,51,1)
            print(new_gold)
            request.session['current_gold']+= new_gold
            print(request.session['current_gold'])
            if new_gold <=0:
                output = f"Entered a casino and lost {new_gold} golds... Ouch.. "
                print(output)
            else:
                output = f"Entered a casino and won {new_gold} golds!"
                print(output)
    
    context = {
        "new_gold": new_gold,
        "current_gold": request.session['current_gold'],
        "location": request.POST['location'],
        "paragraph": "<p>dictionary output</p>"
    }
    print(context['location'])
    # print(output)  Create string within session string that adds to each other and repaste every time with past activities JS .html(output)

    return render(request, 'index.html',context)
