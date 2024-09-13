# -------------------------------------------
# slider.py
#
# Contoh pengontrolan kecepatan motor DC
#   menggunakan slider
# -------------------------------------------

import RPi.GPIO as GPIO
import time
import Tkinter

def ubahKecepatan(nilai):
    pwm.ChangeDutyCycle(float(nilai))

def gui():
    # GUI
    jendela = Tkinter.Tk()
    jendela.title('Kontrol Kecepatan Motor')
    jendela.geometry('350x100')

    slider = Tkinter.Scale(jendela, 
                       orient=Tkinter.HORIZONTAL,
                       length=250,
                       resolution = 5,
                       command=ubahKecepatan)
    slider.pack(pady = 10)

    jendela.mainloop()


# Program utama
pinBasis = 17

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBasis, GPIO.OUT)

pwm = GPIO.PWM(pinBasis, 100)
pwm.start(0)

gui()
