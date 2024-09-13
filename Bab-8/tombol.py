# ----------------------------------------
# tombol.py
#
# Contoh untuk mengendalikan LED
#   berdasarkan keadaan tombol 
# ----------------------------------------

import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

# Pastikan LED mati
GPIO.output(17, GPIO.LOW)

while True:
    # Baca keadaan tombol
    keadaanTombol = GPIO.input(4)

    # Proses LED
    if keadaanTombol == 1: 
        # Hidupkan LED
        GPIO.output(17, GPIO.HIGH)
    else:
        # Matikan LED
        GPIO.output(17, GPIO.LOW)
