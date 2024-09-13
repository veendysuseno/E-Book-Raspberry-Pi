# ----------------------------------------
# led.py
#
# Contoh untuk membuat LED berkedip-kedip
# ----------------------------------------

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
    # Hidupkan LED 
    GPIO.output(17, GPIO.HIGH)
    time.sleep(1)

    # Hidupkan LED 
    GPIO.output(17, GPIO.LOW)
    time.sleep(1)
