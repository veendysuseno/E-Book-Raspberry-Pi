# -----------------------------------
# terkecil
#
# Contoh penentuan bilangan terkecil
#    dari dua bilangan
# -----------------------------------

def perolehTerkecil(a, b):
    terkecil = a
    if b < terkecil:
        terkecil = b

    # Nilai balik
    return terkecil

# Tes fungsi
print 'Terkecil dari 5 dan 3 = ', \
      perolehTerkecil(5, 3)

print 'Terkecil dari 3 dan 5 = ', \
      perolehTerkecil(3, 5)
