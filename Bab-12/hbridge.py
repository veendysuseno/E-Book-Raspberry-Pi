# ----------------------------------------
# hbridge.py
#
# Pengontrolan motor DC menggunakan L298N
# ----------------------------------------

import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

pinIN1 = 17
pinIN2 = 18
pinENA = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinIN1, GPIO.OUT)
GPIO.setup(pinIN2, GPIO.OUT)
GPIO.setup(pinENA, GPIO.OUT)

pwm = GPIO.PWM(pinENA, 100)
pwm.start(20)

while True:
   # Putar ke satu arah
   GPIO.output(pinIN1, GPIO.HIGH)
   GPIO.output(pinIN2, GPIO.LOW)
   time.sleep(3)

   # Stop
   GPIO.output(pinIN1, GPIO.LOW)
   GPIO.output(pinIN2, GPIO.LOW)
   time.sleep(3)

   # Putar ke arah lain
   GPIO.output(pinIN1, GPIO.LOW)
   GPIO.output(pinIN2, GPIO.HIGH)
   time.sleep(3)

   # Stop
   GPIO.output(pinIN1, GPIO.LOW)
   GPIO.output(pinIN2, GPIO.LOW)
   time.sleep(3)
