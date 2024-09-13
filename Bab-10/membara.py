# --------------------------------
# membara.py
#
# Contoh penggunaan PWM
#   untuk membuat api yang membara
# --------------------------------

import RPi.GPIO as GPIO
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

ledPWM1 = GPIO.PWM(17, 200)
ledPWM1.start(50)
ledPWM2 = GPIO.PWM(18, 200)
ledPWM2.start(50)
ledPWM3 = GPIO.PWM(27, 200)
ledPWM3.start(50)

while True:
   ledPWM1.ChangeDutyCycle(
      10 + random.randint(0, 90))
   ledPWM2.ChangeDutyCycle(
      10 + random.randint(0, 90))
   ledPWM3.ChangeDutyCycle(
      10 + random.randint(0, 90))
