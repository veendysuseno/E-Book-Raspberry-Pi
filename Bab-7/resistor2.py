
# -----------------------------------
# resistor2
#
# Contoh penggunaan if..elif..else
# -----------------------------------

hambatan = input('Berapa hambatan resistor? ')

if hambatan < 220:
    print 'Hambatan terlalu kecil. Gunakan aling tidak 220 ohm'
elif hambatan > 1000:
    print 'LED mungkin tak menyala. Gunakan paling besar 1K'
else:
    print 'OK, boleh digunakan. LD pasti menyala'
