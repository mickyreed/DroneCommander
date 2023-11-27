from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser, Drone, Swarm, AP
from .forms import UserForm, DroneForm, SwarmForm, AccountAuthenticationForm, APForm, RegisterForm
from django.contrib.auth import get_user_model, authenticate, logout
from django.contrib import messages
import time
from django.http import HttpResponse
from django.db import IntegrityError
import requests
from django.http import JsonResponse
from djitellopy import Tello
import asyncio


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


def ap_edit(request, id):
    ap = AP.objects.get(id=id)
    form = APForm(request.POST or None, instance=ap)
    if form.is_valid():
        try:
            form.save()
            return redirect('ap_list')
        except:
            pass
    return render(request,'main/ap_edit.html', {'ap': ap, 'form': form})


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


def control(request):
    active_drones = Drone.objects.all()
    swarms = Swarm.objects.all()

    # Get the drones belonging to the selected swarm
    selected_swarm_drones = Drone.objects.filter(swarm_id=1)

    # Pass the data to the template
    # return render(request, 'main/control.html', {'swarms': swarms, 'selected_swarm_drones': selected_swarm_drones})

    if request.method == 'POST':
        # Assuming you have a form with a button that triggers the POST request
        command = request.POST.get('command')

        # Send the command to the mock drone server
        response = requests.post('http://127.0.0.1:8890/', data=command.encode('utf-8'))

        # Display the response from the mock drone on the front end
        telemetry_data = response.text
        return render(request, 'main/control.html', {'telemetry_data': telemetry_data, 'drones': active_drones, 'swarms': swarms, 'selected_swarm_drones':selected_swarm_drones})

    return render(request, 'main/control.html', {'drones': active_drones, 'swarms': swarms, 'selected_swarm_drones': selected_swarm_drones})

def launch_swarm(request):

    if request.method == 'POST':
        # Get the selected swarm ID from the form data
        selected_swarm_id = request.POST.get('selected_swarm')

        # Get the drones belonging to the selected swarm
        selected_swarm_drones = Drone.objects.filter(swarm_id=selected_swarm_id)

        # Initialize telemetry_data
        telemetry_data_list = []

        # Initialize flight_data
        # flight_data = {}

        # Launch each drone in the swarm
        for drone in selected_swarm_drones:
            flight_data = launch_drone(drone.IPAddress)  # Assuming you have a function to launch a drone
            telemetry_data_list.append({drone.droneName: flight_data.get('telemetry_data')})

        # Return a JSON response
        print(telemetry_data_list)
        return JsonResponse({'status': 'success', 'telemetry_data_list': telemetry_data_list})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



def launch_drone(ip_address):
    # Simulate the launch command for demonstration
    PORT = 8999
    print(f'******   Drone at {ip_address, PORT} launched!   ******')

    # Assuming you want to connect to a single drone (replace this logic as needed)
    drone = Tello(ip_address)
    drone.connect()

    # create a flight_log list
    flight_log = []

    try:
        # Run the box flight formation
        flight_log.append("Taking off...")
        drone.takeoff()
        flight_log.append("Moving up...")
        drone.move_up(50)
        flight_log.append("Moving forward...")
        drone.move_forward(50)
        flight_log.append("Rotating clockwise...")
        drone.rotate_clockwise(90)
        flight_log.append("Moving forward...")
        drone.move_forward(50)
        flight_log.append("Rotating clockwise...")
        drone.rotate_clockwise(90)
        flight_log.append("Moving forward...")
        drone.move_forward(50)
        flight_log.append("Rotating clockwise...")
        drone.rotate_clockwise(90)
        flight_log.append("Moving forward...")
        drone.move_forward(50)
        flight_log.append("Landing...")
        drone.land()

        # Query the battery level
        battery_level = drone.get_battery()

        # Print the battery level
        print(f"Battery Level: {battery_level}%")
        # flight_log.append("Battery...")

        # Query telemetry data
        try:
            battery_level = drone.get_battery()
            flight_time = drone.get_flight_time()

        except Exception as e:
            print(f"Error getting telemetry data: {e}")
            battery_level, flight_time, = None, None

        # Return a JSON response with flight log
        response_data = {
            'status': 'success',
            'flight_log': flight_log,
            'telemetry_data': {
            'battery_level': battery_level,
            'flight_time': flight_time,
            }
        }
        return response_data
    except Exception as e:
        # Handle exceptions (e.g., if the drone disconnects unexpectedly)
        response_data = {'status': 'error', 'message': str(e)}
        return response_data

def connect(request):
    if request.method == 'POST':
        drone = request.POST.get('drone_id')

        return HttpResponse(f"Connected to {drone.DroneName}")
    else:
        return HttpResponse("Invalid Request Method", status=405)
