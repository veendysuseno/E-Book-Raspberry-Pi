# -----------------------------------------
# potensio.py
#
# Contoh untuk memantau nilai potensiometer
# -----------------------------------------

import spidev

def bacaAnalog(kanal):
    data = spi.xfer2([1, (8 + kanal) << 4, 8])
    hasil_adc = ((data[1] & 3) << 8) + data[2]
    return hasil_adc

spi = spidev.SpiDev()
spi.open(0,0)

while True:
   nilaiPotensio = bacaAnalog(0)
   tegangan = nilaiPotensio * 3.3 / 1024
   print 'Tegangan =', tegangan
   raw_input('Tekan Enter untuk membaca lagi...')
