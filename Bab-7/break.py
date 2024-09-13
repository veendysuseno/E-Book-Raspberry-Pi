# -----------------------------------
# break
#
# Contoh penggunaan break pada for
# -----------------------------------

for nilai in [ 1, 2, 3, 4, 5]:
    if nilai == 3:
        print 'break dieksekusi... '
        break

    print nilai
else:
    print '*** Selesai... '
