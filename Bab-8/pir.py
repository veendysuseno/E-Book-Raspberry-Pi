# ----------------------------------------
# pir.py
#
# Contoh penggunaan PIR (Passive infrared)
# ----------------------------------------

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

# Pastikan LED mati
GPIO.output(17, GPIO.LOW)

while True:
    # Baca output PIR
    statusPIR = GPIO.input(4)

    if statusPIR == 1:
        GPIO.output(17, GPIO.HIGH)
        time.sleep(2)
    else:
        GPIO.output(17, GPIO.LOW) 
