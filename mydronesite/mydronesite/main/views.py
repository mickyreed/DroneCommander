from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import CustomUser as User
from .models import CustomUser, Drone, Swarm, AP
from django.contrib.auth.models import User
from .forms import UserForm, DroneForm, SwarmForm, AccountAuthenticationForm, APForm
from .forms import RegisterForm
from django.contrib.auth import get_user_model, authenticate, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from djitellopy import Tello
from examples import simple
# from .tello_control import TelloController
import time
from django.db import IntegrityError
import requests



# Create your views here.

def user_list(request):
    users = get_user_model().objects.all()
    return render(request, 'main/user_list.html', {'users': users})

def drone_list(request):
    drones = Drone.objects.all()
    return render(request, 'main/drone_list.html', {'drones': drones})

def swarm_list(request):
    swarm = Swarm.objects.all()
    return render(request, 'main/swarm_list.html', {'swarm': swarm})

def user_add(request):
    print('user_add')
    context ={}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('user_list')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})


def register(response):
    print('register')
    context ={}
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                pass
    else:
        form = RegisterForm()
    return render(response, 'registration/register.html', {'form': form})


def drone_add(request):
    print('drone_add')
    context ={}
    if request.method == 'POST':
        form = DroneForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('drone_list')
            except IntegrityError:
                messages.error(request, 'Drone with the same name already exists.')
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
                return redirect('swarm_list')
            except IntegrityError:
                messages.error(request, 'Swarm with the same name already exists.')
    else:
        form = SwarmForm()
    return render(request, 'main/swarm_add.html', {'form': form})


def user_edit(request, id):
    user = get_user_model().objects.get(id=id)
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
    user = get_user_model().objects.get(id=id)
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
    user = get_user_model().objects.get(id=id)
    user.delete()
    return redirect('user_list')


def drone_delete(request, id):
    drone = Drone.objects.get(id=id)
    drone.delete()
    return redirect('drone_list')


def swarm_delete(request, id):
    swarm = Swarm.objects.get(id=id)
    swarm.delete()
    return redirect('swarm_list')


def home(request):

    users = get_user_model().objects.all()
    drone = Drone.objects.all()
    return render(request, 'main/index.html', {'drone': drone, 'users': users})
    # swarm = Swarm.objects.all()
    # return render(request, 'main/home.html', {'swarm': swarm})


def login(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():

                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(email=email, password=password)
                if user:
                    login(request)

                    return redirect('main/home')

    else:
        form = AccountAuthenticationForm()

        context['login'] = form
    return render(request, "registration/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('home')


def index(request):
    # all_users = User.objects.all()
    user = get_user_model().objects.get()
    drone = Drone.objects.all()
    swarm = Swarm.objects.all()
    return render(request, 'main/index.html', {'user': user, 'drone': drone, 'swarm': swarm})


def ap_list(request):
    ap = AP.objects.all()
    return render(request, 'main/ap_list.html', {'ap': ap })


def ap_list(request):
    ap = AP.objects.all()
    return render(request, 'main/ap_list.html', {'ap': ap })


def ap_edit(request, id):
    ap = AP.objects.get(id=id)
    form = APForm(request.POST or None, instance=ap)
    if form.is_valid():
        try:
            form.save()
            return redirect('ap_list')
        except:
            pass
    return render(request,'main/ap_list.html', {'ap': ap, 'form': form})


def ap_add(request):
    print('ap_add')
    context ={}
    if request.method == 'POST':
        form = APForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('ap_list')
            except IntegrityError:
                messages.error(request, 'AP with the same name already exists.')
    else:
        form = APForm()
    return render(request, 'main/ap_add.html', {'form': form})


def ap_delete(request, id):
    ap = AP.objects.get(id=id)
    ap.delete()
    return redirect('ap_list')


# create an instance of the tello controller
# tello_control = TelloController()
active_drones = []


# def control(request):
#     if request.method == 'POST':
#         # Assuming you have a form with a button that triggers the POST request
#         command = request.POST.get('command')
#
#         # Send the command to the mock drone server
#         response = requests.post('http://127.0.0.1:8890/', data=command.encode('utf-8'))
#
#         # Display the response from the mock drone on the front end
#         telemetry_data = response.text
#         return render(request, 'control.html', {'telemetry_data': telemetry_data})
#
#     return render(request, 'control.html')




# def control(request):
#     telemetry_data = []
#     all_drones = Drone.objects.all()
#     print(all_drones)
#     return render(request, "main/control.html",{'drones': all_drones})


# @login_required
# def connect(request):
#     if request.method == 'POST':
#         tello_control.connect()
#         return JsonResponse({'message': 'Drone connected successfully'})
#     else:
#         return HttpResponse(status=405)  # Method Not Allowed for non-POST requests


# @login_required
def launch(request):
    if request.method == 'POST':
        tello_control.takeoff()
        tello_control.move_box()
        tello_control.land()
        return JsonResponse({'message': 'Drone launched successfully'})
    else:
        return HttpResponse(status=405)  # Method Not Allowed for non-POST requests


def connect(request):
    if request.method == 'POST':
        # Assuming the form sends the 'drone_id' as part of the POST data
        drone_id = request.POST.get('drone_id')
        drone = get_object_or_404(Drones, DroneID=drone_id)

        connected_drones[drone_id] = TelloDrone(host=drone.IPAddress)
        return HttpResponse(f"Connected to {drone.DroneName}")
    else:
        return HttpResponse("Invalid Request Method", status=405)


from django.http import HttpResponse


def send_command(request):
    if request.method == 'POST':
        selected_drone_id = request.POST.get('selected_drone_id')
        command = request.POST.get('command')

        if selected_drone_id not in connected_drones:
            return HttpResponse("Drone not connected yet")

        drone = connected_drones[selected_drone_id]

        if command == 'takeoff':
            drone.takeoff()
        elif command == 'land':
            drone.land()
        # Add other commands and their execution logic here
        else:
            return HttpResponse("Invalid command")

        response_text = f"Command '{command}' executed on Drone ID: {selected_drone_id}"
        return HttpResponse(response_text)
    else:
        return HttpResponse("Invalid Request Method", status=405)
