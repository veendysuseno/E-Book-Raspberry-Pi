# -----------------------------------
# touch.py
#
# Contoh pengendalian LED
#   dengan sensor sentuh
# -----------------------------------

import RPi.GPIO as GPIO
import time

keadaanSebelum = GPIO.HIGH
waktuTerakhir = time.time()
INTERVAL = 0.5

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

GPIO.output(17, GPIO.LOW)

while True:
   nilaiSaklarSentuh = GPIO.input(4) 
 
   waktuSekarang = time.time()
   if (nilaiSaklarSentuh == GPIO.LOW) and \
      (waktuSekarang - waktuTerakhir > INTERVAL):
       if keadaanSebelum == GPIO.HIGH:
           statusLedSekarang = GPIO.LOW
       else:
           statusLedSekarang = GPIO.HIGH

       keadaanSebelum = statusLedSekarang

       # Menyalakan atau mematikan LD
       GPIO.output(17, statusLedSekarang)

       waktuTerakhir = time.time()
 
