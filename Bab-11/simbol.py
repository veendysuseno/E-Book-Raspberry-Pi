# ---------------------------------------
# simbol.py
#
# Contoh pembuatan simbol
# ---------------------------------------

from RPLCD import CharLCD
import RPi.GPIO as GPIO

hurufA = ( 
  0b01110, 0b01010, 0b01010, 0b01010, 
  0b11111, 0b11001, 0b11001, 0b11001)
 
hurufC = (
  0b01111, 0b11001, 0b11000, 0b11000,
  0b11000, 0b11000, 0b11001, 0b11111)

hurufE = (
  0b01111, 0b11001, 0b11000, 0b11000,
  0b11110, 0b11000, 0b11001, 0b11111)

hurufI = (
  0b11111, 0b00100, 0b00100, 0b01100,
  0b01100, 0b01100, 0b01100, 0b11111)

hurufR = (
  0b01111, 0b11001, 0b11001, 0b11001,
  0b11110, 0b11010, 0b11001, 0b11001)

GPIO.setwarnings(False)

lcd = CharLCD(17, None, 18, [27, 22, 23, 24],
              GPIO.BCM, 16, 2, 8)

# Tentukan simbol
lcd.create_char(0, hurufA)
lcd.create_char(1, hurufC)
lcd.create_char(2, hurufE)
lcd.create_char(3, hurufI)
lcd.create_char(4, hurufR)

# Tampilkan simbol
lcd.write(1)
lcd.write(2)
lcd.write(4)
lcd.write(3)
lcd.write(0)

lcd.cursor_pos = (1, 0)
lcd.write_string(unichr(1)+ ' ' + \
                 unichr(2)+ ' ' + \
                 unichr(4)+ ' ' + \
                 unichr(3)+ ' ' + \
                 unichr(0)) 
