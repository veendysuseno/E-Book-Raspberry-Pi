# -----------------------------------
# konstruk
#
# Contoh kelas yang melibatkan
#    konstruktor dan destruktor
# -----------------------------------

# Definisi kelas
class Komponen:
   nama = ''
   nilai = ''
   jumlah = 0
   total_objek = 0
   
   # Konstruktor
   def __init__(self, nama, nilai, jumlah):
       self.nama = nama
       self.nilai = nilai
       self.jumlah = jumlah

       Komponen.total_objek += 1
       
   # Destruktor
   def __del__(sel):
       Komponen.total_objek -= 1

   # Metode biasa    
   def info(self):
       print 'Nama  : ', self.nama
       print 'Nilai : ', self.nilai
       print 'Jumlah: ', self.jumlah
       print 'Total objek = ', Komponen.total_objek
       print

# Pembuatan objek
resA = Komponen('Resistor', '2K', 6)
tran = Komponen('Transistor', 'TIP120', 5)

# Pemanggilan metode
resA.info()
tran.info()

del resA # Hapus objek resA
tran.info()

del tran # Hapus objek tran
print 'Total objek sekarang: ', Komponen.total_objek
