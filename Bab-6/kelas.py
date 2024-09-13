
# -----------------------------------
# kelas
#
# Contoh pembuatan kelas dan objek
# -----------------------------------

# Definisi kelas
class Komponen:
   nama = ''
   nilai = ''
   jumlah = 0

   def info(self):
       print 'Nama  : ', self.nama
       print 'Nilai : ', self.nilai
       print 'Jumlah: ', self.jumlah
       print

# Pembuatan objek
r2 = Komponen()

# Pengaturan nilai di atribut
r2.nama = 'Resistor'
r2.nilai = '2K'
r2.jumlah = 5

# Pemanggilan metode
r2.info()

