# ---------------------------------------
# lcd2.py
#
# Contoh penggunaan efk scrolling
# ---------------------------------------

from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

lcd = CharLCD(17, None, 18, [27, 22, 23, 24],
              GPIO.BCM, 16, 2, 8)

lcd.write_string('0123456789012345')
lcd.cursor_pos = (1, 0)
lcd.write_string('ABCDEFGHIJKLMNOP')

time.sleep(2)
for num in range(1, 17):
    lcd.shift_display(1)
    time.sleep(1)

for num in range(1, 17):
    lcd.shift_display(-1)
    time.sleep(1)


lcd.close()
