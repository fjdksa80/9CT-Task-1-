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

# Main loop
while True:
    while colour_sensor.reflection() < 50 and ultrasonic_sensor.distance() > 50:
        robot.drive()
    if ultrasonic_sensor.distance() <= 50:
        colour_sensor_motor.run_angle(-90)
        if colour_sensor.Color() == Color.RED or Color.YELLOW:
            ev3.speaker.beep()
        else:
            robot.straight(-50)
            robot.turn(90)
    if colour_sensor.reflection() >= 50:
        robot.straight(-50)
        robot.turn(90)
    