''' Default argument'''

#  def fungsi (argument)
#  def fungsi (argument = nilai default)

#contoh 1
def say_halo(nama = "kamu"):
    '''fungsi dengan default argument'''
    print(f"haloooo {nama}")

say_halo("ucup")
say_halo()

# contoh 2
def sapa_dia(nama,pesan = "apakabar"):
    '''fungsi dengan satu input biasa dan satu default argument'''
    print(f"hai {nama} ,{pesan}")

sapa_dia("hai ganteng ", "aseps")

sapa_dia("alieee")


def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,2))