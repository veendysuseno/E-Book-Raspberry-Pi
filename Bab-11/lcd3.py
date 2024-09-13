# ---------------------------------------
# lcd3.py
#
# Contoh menampilkan tulisan yang panjang
# ---------------------------------------

from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

teks = 'Selamat mempelajari cara memprogram LCD Display. '
teks = teks +\
   'Cobalah semua contoh di bab ini untuk memahaminya. ' +\
   'Kemudian, Anda bisa mengembangkannya sendiri ' +\
   'sesuai dengan ide Anda. Sekali lagi, selamat belajar ' +\
   'dan sukses selalu!'

indeks = 0
 
GPIO.setwarnings(False)

lcd = CharLCD(17, None, 18, [27, 22, 23, 24],
              GPIO.BCM, 16, 2, 8)
lcd.write_string('Info untuk Anda:')

try:
    while True:
        st = ''
        # Bentuk string
        for j in range(0, 16):
            if indeks + j < len(teks):
                st = st + teks[indeks + j]
            else:
                st = st + ' '
  
            # Tampilkan di baris kedua
            lcd.cursor_pos = (1, 0)
            lcd.write_string(st)
  
        # Peroleh indeks berikutnya
        indeks = indeks + 1
        if indeks == len(teks) - 1:
            indeks = 0;

        time.sleep(1)
except KeyboardInterrupt:
    pass

lcd.close()
