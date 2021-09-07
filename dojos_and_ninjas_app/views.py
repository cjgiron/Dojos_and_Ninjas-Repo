from django.shortcuts import render, redirect
from .models import *


def index(request):

    context = {
        "all_dojos": Dojo.objects.all(),
        "all_ninjas": Ninja.objects.all()
    }

    return render(request, 'index.html', context)


def process_dojo(request):
    print(request.POST)

    Dojo.objects.create(
        name = request.POST['dojo_name'],
        city = request.POST['dojo_city'],
        state = request.POST['dojo_state']
    )

    return redirect('/')

def process_ninja(request):
    
    ninja_dojo = Dojo.objects.get(id=request.POST['dojo_id'])

    Ninja.objects.create (
        first_name = request.POST['ninja_first_name'],
        last_name = request.POST['ninja_last_name'],
        dojo = ninja_dojo
    )

    return redirect("/")