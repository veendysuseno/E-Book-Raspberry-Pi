# ---------------------------------------
# lcd4.py
#
# Contoh menampilkan simbol-simbol khusus
# ---------------------------------------

from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time
 
GPIO.setwarnings(False)

lcd = CharLCD(17, None, 18, [27, 22, 23, 24],
              GPIO.BCM, 16, 2, 8)

bil = 220
akhir = bil + 32

while (bil < akhir):
    lcd.write(bil)
    bil = bil + 1
