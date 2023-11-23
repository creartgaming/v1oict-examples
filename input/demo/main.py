from machine import Pin
import time

led_pin = Pin(20, Pin.OUT)
switch_pin_on = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
switch_pin_off = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    if switch_pin_on.value():
        led_pin.value(1)
    elif switch_pin_off.value():
        led_pin.value(0)

