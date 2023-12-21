import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

while True:
    np[0] = [0, 128, 0]
    np[1] = [0, 128, 0]
    np[2] = [0, 128, 0]
    np[3] = [0, 128, 0]
    np[4] = [255, 0, 0]
    np[5] = [255, 0, 255]
    np[6] = [255, 0, 0]
    np[7] = [255, 0, 0]

    np.write()

    time.sleep(1)