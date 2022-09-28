from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05

while True:
    cp.pixels[0] = (255, 0, 0)
    cp.pixels[1] = (0, 255, 0)
    cp.pixels[3] = (0, 255, 255)
    cp.pixels[4] = (255, 255, 0)
    cp.pixels[2] = (255, 0, 255)
