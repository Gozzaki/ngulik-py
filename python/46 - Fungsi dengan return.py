''' fungsi dengan kembalian '''

# tempalete fungsi dengan kembalian 

# def nama_fungsi(argument):
#       badan fungsi
#       return output

def kuadrat(input_angka):
    output = input_angka**2
    return output

y = kuadrat(5)
print(y)
print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah 

def fungsi_tambah(angka_1,angka_2):
    return angka_1 + angka_2

a = fungsi_tambah(10,7)
print(a)

# fungsi dengan return banyak

def operasi_matematika(angka_1:int,angka_2:int)->int:
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah,kurang,kali,bagi
k,l,m,n= operasi_matematika(9,5)
print(f"Hasil tambah ={k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")

def fungsi(*args):
    angka1 = args[0]
    angka2 = args[1]
    return  angka1 + angka2

fungsi(1,2)
print(f"ii   {fungsi(1,3)}")