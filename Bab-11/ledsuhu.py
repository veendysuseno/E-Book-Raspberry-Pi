# ---------------------------------------
# lcdsuhu.py
#
# Contoh untuk menampilkan suhu di LCD
# ---------------------------------------

from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time
import spidev

def bacaAnalog(kanal):
    data = spi.xfer2([1, (8 + kanal) << 4, 8])
    hasil_adc = ((data[1] & 3) << 8) + data[2]
    return hasil_adc

# Program utama
GPIO.setwarnings(False)

spi = spidev.SpiDev()
spi.open(0,0)

lcd = CharLCD(17, None, 18, [27, 22, 23, 24],
              GPIO.BCM, 16, 2, 8)

while True:
    nilaiSensor = bacaAnalog(0)
    celcius = 100 * nilaiSensor * 5.0 / 1024
    
    info = 'Suhu = ' + '{:.2f}'.format(celcius)
    lcd.clear()
    lcd.write_string(info)
    lcd.write(223) # Simbol derajat

    time.sleep(1)
