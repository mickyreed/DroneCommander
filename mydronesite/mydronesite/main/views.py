from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Drone, Swarm
from django.contrib.auth.models import User
from .forms import UserForm, DroneForm, SwarmForm

# Create your views here.

def user_list(request):
    all_users = User.objects.all()
    return render(request, 'main/user_list.html', {'all_users': all_users})

def add_user(request):

    context ={}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'main/registration.html', {'form': form})


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

def home(request):
    all_users = User.objects.all()
    return render(request, 'main/home.html', {'all_users': all_users})

def login(response):
    return render(response, "main/add_user.html", {})

def index(request):
    all_users = User.objects.all()
    return render(request, 'main/index.html', {'all_users': all_users})