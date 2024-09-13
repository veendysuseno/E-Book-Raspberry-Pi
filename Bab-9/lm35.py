# ------------------------------------
# lm35.py
#
# Contoh pengukuran suhu dengan LM35DZ
# ------------------------------------

import spidev
import Tkinter

def bacaAnalog(kanal):
    data = spi.xfer2([1, (8 + kanal) << 4, 8])
    hasil_adc = ((data[1] & 3) << 8) + data[2]
    return hasil_adc

def perbaharuiInfo():
    nilaiSensor = bacaAnalog(0)
    celcius = 100 * nilaiSensor * 5.0 / 1024
    label.config(text = "{:.2f}".format(celcius))
    jendela.after(500, perbaharuiInfo)

# Program utama
spi = spidev.SpiDev()
spi.open(0,0)

# Buat jendela
jendela = Tkinter.Tk()
jendela.title('Suhu')
jendela.geometry('250x80')
label = Tkinter.Label(jendela, text = 'Tes')
label.pack(pady = 20)
jendela.after(500, perbaharuiInfo)

jendela.mainloop()
