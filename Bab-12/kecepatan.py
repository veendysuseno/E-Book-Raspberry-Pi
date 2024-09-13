# -------------------------------------------
# kecepatan.py
#
# Contoh pengontrolan kecepatan motor DC
# -------------------------------------------

import RPi.GPIO as GPIO
import time

pinBasis = 17

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBasis, GPIO.OUT)

pwm = GPIO.PWM(pinBasis, 100)
pwm.start(0)

try:
    while True:
        # kecepatan tinggi
        pwm.ChangeDutyCycle(100)	
        time.sleep(3)

        # kecepatan sedang
        pwm.ChangeDutyCycle(50)	
        time.sleep(3)

        # Stop motor
        pwm.ChangeDutyCycle(0)	
        time.sleep(3)
        
except KeyboardInterrupt:
    GPIO.cleanup()
