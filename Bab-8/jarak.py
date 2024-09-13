# -----------------------------------
# jarak.py
#
# Contoh penggunaan sensor ultrasonik
#   untuk mengukur jarak
# -----------------------------------

import RPi.GPIO as GPIO
import time

pinTrig = 17
pinEcho = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinTrig, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

while True:
   GPIO.output(pinTrig, GPIO.LOW)
   time.sleep(0.5)

   GPIO.output(pinTrig, GPIO.HIGH)
   time.sleep (0.00001)
   GPIO.output(pinTrig, GPIO.LOW)

   while GPIO.input(pinEcho) == GPIO.LOW:
      waktuMulai = time.time()

   while GPIO.input(pinEcho) == GPIO.HIGH:
      waktuAkhir = time.time()

   waktu = waktuAkhir - waktuMulai

   jarak = 17150 * waktu
   print 'Jarak', jarak, "cm"

   raw_input('Tekan Enter untuk mengukur lagi...')
