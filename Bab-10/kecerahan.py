# -------------------------------
# kecerahan.py
#
# Contoh penggunaan PWM
#   untuk mengatur kecerahan LED
# -------------------------------

import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

ledPWM = GPIO.PWM(17, 200)
ledPWM.start(50)

while True:
   siklus = raw_input("Kecerahan (0 s/d 100): ")
   ledPWM1.ChangeDutyCycle(int(siklus))
