# -----------------------------------
# cari
#
# Contoh penggunaan break
#    pada pencarian komponen
# -----------------------------------

daftarKomponen = ['LED merah', 'LED hijau', 'Resistor 100 ohm',
                  'Transistor TIP120', 'Kapasitor 1mF']
dicari = raw_input('Komponen yang dicari: ')

indeks = 0
ditemukan = False

while indeks < len(daftarKomponen):
    if dicari in daftarKomponen[indeks]:
        ditemukan = True
        break

    indeks = indeks + 1

if ditemukan:
    print 'Komponen yang cocok: ', daftarKomponen[indeks]
else:
    print 'Maaf, nggak ada '
