# -----------------------------------
# rintangan.py
#
# Contoh penggunaan sensor ultrasonik
#   untuk mengukur jarak
# -----------------------------------

import RPi.GPIO as GPIO

pinLed = 17
pinSensor = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(pinSensor, GPIO.IN)

# Matikan LED
GPIO.output(pinLed, GPIO.LOW)

while True:
   statusSensor = GPIO.input(pinSensor)
   if statusSensor == GPIO.HIGH:
       GPIO.output(pinLed, GPIO.LOW)
   else:
       GPIO.output(pinLed, GPIO.HIGH)
