import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

while True:

    for x in range(len(np)):
        np[x] = [100, 0, 0]

        np.write()

        time.sleep(0.5)

    for x in range(len(np)):
        np[x] = [0, 0, 0]

        np.write()

        time.sleep(0)