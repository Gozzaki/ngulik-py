# Lambda Function

def f_kuadrat(angka):
    return angka**2

print(f"Hasil Fungsi Kuadrat  ={f_kuadrat(3)}")

#kita coba dengan Lambda
#output = lamda argument : expression
kuadrat = lambda angka : angka**2
print(f"hasil lambda kuadrat = {kuadrat(3)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda kuadrat = {pangkat(4,2)}")

## Kegunaan Lambda

# Sorting untuk List biasa
data_list = ['ali','zudueng','ucups']
data_list.sort()
print(f"sorted list =  data list = {data_list}")

# sorting pakai panjang
def panjang_nama(nama):
    return len(nama)

#print(f"menggunakan fungsi {panjang_nama(data_list)}")
data_list.sort(key=panjang_nama)
print(f"sorted list by panjang data list = {data_list}")

#sort pakai lambda
data_list = ['aliii','zuduengg','ucupss']
data_list.sort(key=lambda nama:len(nama))
print(f"sorted panjang list by lambda = {data_list}")

#filter pakai fungsi
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
def kurang_dari_lima(angka):
    return angka < 5
# data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_baru = list(filter(lambda x:x <16,data_angka))
print(data_angka_baru)

#kasus genap 
data_genap = list(filter(lambda x: (x%2==0),data_angka))
print(data_genap)

#kasus ganjil 
data_ganjil = list(filter(lambda x: (x%2!=0),data_angka))
print(data_ganjil)

# keipatan 3
data_3 = list(filter(lambda x: (x%3==0),data_angka))
print(data_3)

# anonymous function
# currying <- Haskel Curry



# dengan currying menjadi

def pangkat(n):
    return lambda angka:angka ** n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")


