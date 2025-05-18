#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Variables
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
colour_sensor = ColorSensor(Port.S3)
ultrasonic_sensor = UltrasonicSensor(Port.S2)
colour_sensor_motor = Motor(Port.A)
blocks_collected = 0

# Functions
def driving():
    while colour_sensor.reflection() < 50 and ultrasonic_sensor.distance() > 50: # While loop that breaks when the robot detects the edge of the map or an obstacle.
        robot.drive()

def check_obstacles():
    if ultrasonic_sensor.distance() <= 50: # Checks if there's an obstacle
        colour_sensor_motor.run_angle(-90)
        if colour_sensor.Color() == Color.RED or Color.YELLOW:
            ev3.screen.print("Block found!")
        else:
            ev3.screen.print("Wrong colour!")
            robot.straight(-50)
            robot.turn(90)

def check_edge():
    if colour_sensor.reflection() >= 50: # Checks if the robot has reached the edge of the map, and then reverses and turns to avoid leaving the map.
        robot.straight(-50)
        robot.turn(90)  

# Main loop
while blocks_collected < 2:
    driving()
    check_obstacles()
    check_edge()