# Drone Commander
## Introduction
Drone Commander is a Tello drone controller made for Diploma Advanced Programming.
The app uses Django with a custom crud and template to control drone swarms using the DJITelloPy package
## Features
The app features the following
Login and Register functionality for users
Create, update and Delete Drones,, including ability to add to a swarm
Create, update and Delete Swarms
Create, Update and Delete Access Point
Tello Drone Controller where you can view drones and what swarms they belong to, a dropdown menu to select a swarm to launch and a launch button.
A Telemetry Flight Data feedback section which displays flight data related to the battery and flight time at the end of each launch.

## Installation
git clone https://github.com/mickyreed/msr_drone_1.0.git

cd msr_drone_1.0

pip install - r requirements.txt

Once this has installed, if you got to the file, and from the terminal type:

cd .\mydronesite\
cd .\mydronesite\

python manage.py runserver # this will start the application and prvide a link to the webpage


## Usage
Turn on the Tello Drone and ready it for flight, ensure battery is well charged and the area is clear of objects
Get the IP from the tello drone and enter it into the drones IP so they can connect.
Press Launch and the drone will connect and go through an automated box flight before landing and returning telemetry data.
In the case of a swarm, the drones will launch sequentially (one after the other)
