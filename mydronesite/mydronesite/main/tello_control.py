from djitellopy import Tello

import time


class TelloController:
    def __init__(self):
        self.tello = Tello()

    def connect(self):
        self.tello.connect()

    def takeoff(self):
        self.tello.takeoff()
        time.sleep(2)  # Assuming it takes 2 seconds to take off

    def move_box(self):
        # Assuming a simple box pattern: forward, right, backward, left
        self.tello.move_forward(50)
        time.sleep(2)
        self.tello.move_right(50)
        time.sleep(2)
        self.tello.move_back(50)
        time.sleep(2)
        self.tello.move_left(50)
        time.sleep(2)

    def land(self):
        self.tello.land()
        time.sleep(2)  # Assuming it takes 2 seconds to land

    def get_telemetry(self):
        return {
            'battery': self.tello.get_battery(),
            'height': self.tello.get_height(),
            'tof': self.tello.get_distance_tof(),
            'flight time': self.tello.get_flight_time()
        }