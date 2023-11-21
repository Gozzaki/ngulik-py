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
data_list = ['ali','zudueng','ucups']
data_list.sort()