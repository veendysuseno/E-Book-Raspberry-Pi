# ----------------------------------------
# onoff.py
#
# Contoh untuk membuat tombol
#   berfungsi sebagai tombol on atau off 
#   ketika ditekan
# ----------------------------------------

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

# Variabel pengingat
ledMenyala = 0
keadaanSebelum = 0

# Pastikan LED mati
GPIO.output(17, GPIO.LOW)

while True:
    # Baca keadaan tombol
    keadaanSekarang = GPIO.input(4)

    if (keadaanSekarang != keadaanSebelum) and \
       (keadaanSekarang == 1):
        ledMenyala = 1 - ledMenyala 

        GPIO.output(17, ledMenyala)
    
        time.sleep(0.3)

    keadaanSebelum = keadaanSekarang
