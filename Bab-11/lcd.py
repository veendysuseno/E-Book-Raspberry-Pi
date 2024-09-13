# ---------------------------------------
# lcd.py
#
# Contoh untuk menampilkan tulisan di LCD
# ---------------------------------------

from RPLCD import CharLCD
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

lcd = CharLCD(17, None, 18, [27, 22, 23, 24],
              GPIO.BCM, 16, 2, 8)
lcd.write_string('Tes LCD dengan')
lcd.cursor_pos = (1, 0)
lcd.write_string('Raspberry Pi')

raw_input('Tekan tombol Enter untuk mengakhiri...')
lcd.close()
