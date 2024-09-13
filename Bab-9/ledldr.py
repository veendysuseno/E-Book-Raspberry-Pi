# -----------------------------------
# ledldr.py
#
# Contoh pengendalian LED dengani LDR
# -----------------------------------

import spidev
import RPi.GPIO as GPIO

def bacaAnalog(kanal):
    data = spi.xfer2([1, (8 + kanal) << 4, 8])
    hasil_adc = ((data[1] & 3) << 8) + data[2]
    return hasil_adc

pinLed = 17

# Program utama
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLed, GPIO.OUT)
GPIO.output(pinLed, GPIO.LOW)

spi = spidev.SpiDev()
spi.open(0,0)

while True:
    nilaiSensor = bacaAnalog(0)
    if nilaiSensor > 700:
        GPIO.output(pinLed, GPIO.HIGH)
    else:
        GPIO.output(pinLed, GPIO.LOW)
