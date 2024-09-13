# -------------------------------------------
# motordc.py
#
# Contoh pengontrolan motor dengan transistor
# -------------------------------------------

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        # Hidupkan motor
        GPIO.output(17, GPIO.HIGH)
        time.sleep(3)

        # Hidupkan LED 
        GPIO.output(17, GPIO.LOW)
        time.sleep(3)
except KeyboardInterrupt:
    GPIO.cleanup()
