# -----------------------------------
# deteksi.py
#
# Contoh penggunaan IR line tracking
# -----------------------------------

import spidev
import Tkinter

AMBANG = 500 

def bacaAnalog(kanal):
    data = spi.xfer2([1, (8 + kanal) << 4, 8])
    hasil_adc = ((data[1] & 3) << 8) + data[2]
    return hasil_adc

def perbaharuiInfo():
    nilaiSensor = bacaAnalog(0)
    info = str(nilaiSensor) + ': '
    if nilaiSensor < AMBANG:
        info = info + 'Tidak berada di jalur hitam'
    else:
        info = info + 'Berada di jalur hitam'

    label.config(text = info)
    jendela.after(10, perbaharuiInfo)

# Program utama
spi = spidev.SpiDev()
spi.open(0,0)

# Buat jendela
jendela = Tkinter.Tk()
jendela.title('IR Line Tracking')
jendela.geometry('300x80')
label = Tkinter.Label(jendela, text = 'Tes')
label.pack(pady = 20)
jendela.after(10, perbaharuiInfo)

jendela.mainloop()
