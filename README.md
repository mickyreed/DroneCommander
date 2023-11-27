# msr_drone_1.0
## Introduction
msr-drone_1.0 is a Tello drone controller made for Diploma Advanced Programming.
The app uses Django with a custom crud and template to control drone swarms using the DJITelloPy package
## Features
The app features the following
Login and Register functionality for users
Create, update and Delete Drones,, including ability to add to a swarm
Create, update and Delete Swarms
Create, Update and Delete Access Point
Tello Drone Controller where you can view drones and what swarms they belong to, a dropdown menu to select a swarm to launch and a launch button.
A Telemetry FLight Data feedback section which deisplays flight data related to the battery and flight time at the end of each launch.

## Installation
git clone https://github.com/mickyreed/msr_drone_1.0.git
cd msr_drone_1.0
pip install - r requirements.txt


## Usage
Turn on the Tello Drone and ready it for flight, ensure battery is well charge and the area is clear of objects
Getvthe IP from the tello drone and enter it into the drones IP so they can connect.
Press Launch and the drone will connect and go through an automated box flight before landing and returning telemetry data.
In the case of a swarm, the drones will launch sequentially (one after the other)
