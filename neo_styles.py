from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05

while True:
    if cp.button_b:
        for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)
