# -----------------------------------
# resistor
#
# Contoh penggunaan if..else
# -----------------------------------

hambatan = input('Berapa hambatan resistor? ')

if hambatan < 220:
    print 'Hambatan terlalu kecil. Gunakan aling tidak 220 ohm'
else:
    print 'Aman digunakan, tapi LED mungkin tak menyala'
