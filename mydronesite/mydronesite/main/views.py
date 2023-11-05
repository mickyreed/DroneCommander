from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Drone, Swarm
from .forms import UserForm
from .forms import DroneForm
from .forms import SwarmForm

# Create your views here.

def user_list(request):
    #user = User
    #all_users = User.objects(all)
    return render(request, 'main/user_list.html', {})

def add_user(request):

    context ={}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main/add_user.html')
    else:
        form = UserForm()
    return render(request, 'main/add_user.html', {'form': form})


def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('main/update_user.html')
    else:
        form = UserForm(instance=user)
    return render(request, 'main/update_user.html', {'form': form})


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('main/user_list')
    return render(request, 'main/user_list.html', {'user': user})

def add_drone(request):

    context = {}

    form = DroneForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form

    return render(request, "main/add_drone.html", context)


def add_swarm(request):

    context = {}

    form = SwarmForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form

    return render(request, "main/add_swarm.html", context)

def home(response):
    return render(response, "main/home.html", {})

def login(response):
    return render(response, "main/login.html", {})

