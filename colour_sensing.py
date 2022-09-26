# Color Matching with the Light Sensor: Adafruit Circuit Playground Express
# Created by Stephen @ core-electronics.com.au

from adafruit_circuitplayground.express import cpx
import time
import simpleio

cpx.pixels.fill((0, 0, 0))
cpx.pixels.show()

while True:
    # when button b is pressed, detect color and set ring to that color
    if cpx.button_b:

        # set all cpx.pixels to off
        cpx.pixels.fill((0, 0, 0))
        time.sleep(0.1)

        # turn pixel 1 Red and read light level, turn off after
        cpx.pixels[1] = [255, 0, 0]
        redRaw = cpx.light
        time.sleep(0.1)
        cpx.pixels.fill((0, 0, 0))

        # turn pixel 1 to green and read light leve, turn off after
        cpx.pixels[1] = [0, 255, 0]
        greenRaw = cpx.light
        time.sleep(0.1)
        cpx.pixels.fill((0, 0, 0))

        # turn pixel 1 to blue and read light leve, turn off after
        cpx.pixels[1] = [0, 0, 255]
        blueRaw = cpx.light
        time.sleep(0.1)
        cpx.pixels.fill((0, 0, 0))

        # determine highest light reading
        maximum = max(redRaw, greenRaw, blueRaw)
        minimum = min(redRaw, greenRaw, blueRaw)

        # map light from between minimum light and maximum reading to 0-255
        red = simpleio.map_range(redRaw, minimum, maximum, 0, 255)
        green = simpleio.map_range(greenRaw, minimum, maximum, 0, 255)
        blue = simpleio.map_range(blueRaw, minimum, maximum, 0, 255)

        # this simplifies detected colors into a smaller range,
        # removes washed out colors that just appear white
        if red < 30:
            red = 0
        if green < 30:
            green = 0
        if blue < 30:
            blue = 0

        # converts the float values of red green and blue into intergers
        r = int(red)
        g = int(green)
        b = int(blue)

        # Serial monitor print
        print("Maximum Light: %i" % (maximum))
        print("Minimum Light: %i" % (minimum))
        print("Raw RGB: {0} {1} {2}".format(redRaw, greenRaw, blueRaw))

        # send data to cpx.pixels, display nothing on bad reading
        if maximum - minimum <= 30:
            cpx.pixels.fill((0, 0, 0))
            print("No Color Detected!")
        else:
            cpx.pixels.fill((r, g, b))
            print("Output RGB: {0} {1} {2} ".format(r, g, b))
        print()

    # turn all cpx.pixels off when button A is pressed
    if cpx.button_a:
        cpx.pixels.fill((0, 0, 0))
