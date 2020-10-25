#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port

# Create your objects here.
ev3 = EV3Brick()
touch = TouchSensor(Port.S4)
device = I2CDevice(Port.S1, 0x21)

# Functions
def light_value():
  result = device.read(reg=0x01, length=2)
  return ((result[0] << 8) + result[1])

def led_off():
  device.write(0x02)

def microSwitch():
  result = device.read(reg=0x03, length=1)
  return result[0]

# Write your program here.
while True:
  if touch.pressed() == True:
    val = light_value()
    print(val)
  if touch.pressed() == False:
    led_off();
  if microSwitch() == 0:
    ev3.light.on(Color.RED)
  if microSwitch() == 1:
    ev3.light.off()

