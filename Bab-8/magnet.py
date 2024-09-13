# -----------------------------------
# magnet.py
#
# Contoh pengendalian LED
#   dengan sensor megnet
# -----------------------------------

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.output(17, GPIO.LOW)

while True:
   nilaiSensor = GPIO.input(4) 
 
   if nilaiSensor == GPIO.HIGH:
       GPIO.output(17, GPIO.LOW)
   else:
       GPIO.output(17, GPIO.HIGH)
