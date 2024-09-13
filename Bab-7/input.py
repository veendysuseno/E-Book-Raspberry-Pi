# -----------------------------------
# input
#
# Contoh penanganan eksepsi
# -----------------------------------

while True:
    try:
        bil = raw_input('Masukkan bilangan: ')
        bil = float(bil)
        break # Keluar dari while
    except ValueError:
        print 'Anda salah memasukkan bilangan'

print 'Anda memasukkan bilangan', bil        
