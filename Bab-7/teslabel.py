# ---------------------------
# teslabel
#
# Contoh penambahan Label
# ---------------------------

import Tkinter
aplikasi = Tkinter.Tk()
aplikasi.title('Tes GUI')
aplikasi.geometry('250x100')

# Definisi Label
labelInfo = Tkinter.Label(aplikasi, 
                text = 'Selamat Mencoba!',
                font = ('Helvetica', 18))
labelInfo.pack(pady = 20)

aplikasi.mainloop()
