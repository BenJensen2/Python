from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import ShowManager, Network, Show

def index(request):
    context = {
        'all_shows' : Show.objects.all()
    }
    return render(request,'all_shows.html',context)

def new(request):
    return render(request,'new_show.html')

def create(request):
    print('New Show Added')
    title = request.POST['show_title']
    network = request.POST['show_network'] # Variable name and post name need to be different MultiVarDictError
    release_date = request.POST['show_release_date']
    description = request.POST['show_description']

    print(title, network, release_date, description)
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/new')
    else:

        new_network = Network.objects.create(name=network)
        Show.objects.create(title=title,network=new_network,release_date=release_date,description=description)
        show_id = Show.objects.get(title=title).id

        # network in 
        # check 
        # Show.objects.get(id=show_id).network.add(network)
        return redirect(f'../{show_id}')

def show_info(request,show_id):
    print(f'This is the info for show {show_id}')
    
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request,'show_info.html',context)

def edit(request,show_id):
    print(f'This is where I edit show {show_id}')


    # print(Show.objects.get(id={show_id}))

    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request,'edit_show.html',context)

def update(request,show_id):
    print(f'Show Edited')
    title = request.POST['show_title']
    network_name = request.POST['show_network'] # Variable name and post name need to be different MultiVarDictError
    # network = Network.objects.get(name='network_name')
    release_date = request.POST['show_release_date']
    description = request.POST['show_description']

    # Does Not Work Yet
    # show_to_update=Show.objects.get(id=show_id)
    # show_to_update.title = title
    # show_to_update.network.add(network)
    # show_to_update.release_date = release_date
    # show_to_update.description = description

    print(title)
    print(network_name)
    print(release_date)
    print(description)

    return redirect(f'../../{show_id}')

def destroy(request,show_id):
    print(f'Show {show_id} Destroyed')
    Show.objects.get(id=show_id).delete()
    return redirect('/shows')