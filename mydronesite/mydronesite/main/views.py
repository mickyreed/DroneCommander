from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Drone, Swarm
from django.contrib.auth.models import User
from .forms import UserForm, DroneForm, SwarmForm

# Create your views here.

def user_list(request):
    users = User.objects.all()
    return render(request, 'main/user_list.html', {'users': users})

def drone_list(request):
    drones = Drone.objects.all()
    return render(request, 'main/drone_list.html', {'drones': drones})

def swarm_list(request):
    swarm = Swarm.objects.all()
    return render(request, 'main/swarm_list.html', {'swarm': swarm})

def user_add(request):

    context ={}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'main/registration.html', {'form': form})

def drone_add(request):

    context ={}
    if request.method == 'POST':
        form = DroneForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                pass
    else:
        form = DroneForm()
    return render(request, 'main/drone_add.html', {'form': form})

def swarm_add(request):

    context ={}
    if request.method == 'POST':
        form = SwarmForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                pass
    else:
        form = SwarmForm()
    return render(request, 'main/swarm_add.html', {'form': form})

def user_edit(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        try:
            form.save()
            return redirect('user_list')
        except:
            pass
    return render(request,'main/user_edit.html', {'user': user, 'form': form})

def drone_edit(request, id):
    drone = Drone.objects.get(id=id)
    form = DroneForm(request.POST or None, instance=drone)
    if form.is_valid():
        try:
            form.save()
            return redirect('drone_list')
        except:
            pass
    return render(request,'main/drone_edit.html', {'drone': drone, 'form': form})

def swarm_edit(request, id):
    swarm = Swarm.objects.get(id=id)
    form = SwarmForm(request.POST or None, instance=swarm)
    if form.is_valid():
        try:
            form.save()
            return redirect('swarm_list')
        except:
            pass
    return render(request,'main/swarm_edit.html', {'swarm': swarm, 'form': form})

def user_update(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        try:
            form.save()
            return redirect('user_list')
        except:
            pass
    return render(request, 'main/user_update.html', {'user': user, 'form': form})

def drone_update(request, id):
    drone = Drone.objects.get(id=id)
    form = DroneForm(request.POST or None, instance=drone)
    if form.is_valid():
        try:
            form.save()
            return redirect('drone_list')
        except:
            pass

    return render(request, 'main/drone_update.html', {'drone': drone, 'form': form})

def swarm_update(request, id):
    swarm = Swarm.objects.get(id=id)
    form = SwarmForm(request.POST or None, instance=swarm)
    if form.is_valid():
        try:
            form.save()
            return redirect('swarm_list')
        except:
            pass
    # form = SwarmForm(request.POST or None, instance=swarm)

    return render(request, 'main/swarm_update.html', {'swarm': swarm, 'form': form})


def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('home')


def drone_delete(request, id):
    drone = Drone.objects.get(id=id)
    drone.delete()
    return redirect('home')


def swarm_delete(request, id):
    swarm = Swarm.objects.get(id=id)
    swarm.delete()
    return redirect('home')


# def add_drone(request):
#
#     context = {}
#
#     form = DroneForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context['form']= form
#
#     return render(request, "main/drone_add.html", context)
#
#
# def add_swarm(request):
#
#     context = {}
#
#     form = SwarmForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context['form']= form
#
#     return render(request, "main/swarm_add.html", context)

def home(request):
    users = User.objects.all()
    return render(request, 'main/home.html', {'users': users})
    drone = Drone.objects.all()
    return render(request, 'main/home.html', {'drone': drone})
    swarm = Swarm.objects.all()
    return render(request, 'main/home.html', {'swarm': swarm})

def login(request):
    return render(request, "main/registration.html", {})

def index(request):
    all_users = User.objects.all()
    return render(request, 'main/index.html', {'all_users': all_users})