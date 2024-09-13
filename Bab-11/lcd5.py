# ---------------------------------------
# lcd5.py
#
# Contoh menampilkan simbol panah dan 
#   derajat
# ---------------------------------------

from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time
 
PANAH_KANAN = 0b01111110
DERAJAT = 0b11011111

GPIO.setwarnings(False)

lcd = CharLCD(17, None, 18, [27, 22, 23, 24],
              GPIO.BCM, 16, 2, 8)

lcd.write_string('Suhu ')
lcd.write(PANAH_KANAN)
lcd.write(32)
lcd.write_string(str(23.4))
lcd.write(DERAJAT)
