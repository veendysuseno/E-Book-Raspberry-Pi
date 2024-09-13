# ----------------------------------------
# servo.py
#
# Contoh pengendalian motor servo
# ----------------------------------------

import RPi.GPIO as GPIO
import time

def putarSudut(sudut):
    siklus = sudut / 180.0) + 2.5
    pwm.ChangeDutyCycle(siklus)

GPIO.setwarnings(False)

pinServo = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinServo, GPIO.OUT)
pwm = GPIO.PWM(pinServo, 100)
pwm.start(0)

while True:
   putarSudut(0)
   time.sleep(2)

   putarSudut(90)
   time.sleep(2)

   putarSudut(180)
   time.sleep(2)
