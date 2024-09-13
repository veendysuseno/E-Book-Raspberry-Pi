# -----------------------------------
# ldr.py
#
# Contoh untuk memantau nilai LDR
# -----------------------------------

import spidev
import Tkinter

def bacaAnalog(kanal):
    data = spi.xfer2([1, (8 + kanal) << 4, 8])
    hasil_adc = ((data[1] & 3) << 8) + data[2]
    return hasil_adc

def perbaharuiInfo():
    nilaiSensor = bacaAnalog(0)
    label.config(text = str(nilaiSensor))
    jendela.after(500, perbaharuiInfo)

# Program utama
spi = spidev.SpiDev()
spi.open(0,0)

# Buat jendela
jendela = Tkinter.Tk()
jendela.title('LDR')
jendela.geometry('250x80')
label = Tkinter.Label(jendela, text = 'Tes')
label.pack(pady = 20)
jendela.after(500, perbaharuiInfo)

jendela.mainloop()
