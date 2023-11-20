### OPERASI LIST

# index   0       1       2
data = ["jay","gozzaki","ali"]
#atau     -3      -2      -1     kalo menghitung index dari belakang

#mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

# mengambil data paling akhir
data_0 = data[-1]
print(f"data Terakhir (index -1) = {data_0}")

data_gozzaki = data[-3]

print(f"data jay {data_gozzaki}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")##

## Manipulasi Data
# manambah item pada list sesua posisi
data.insert(0,"Ototng")
print(f"data sesudah di tambah {data}")

# menambah di akhir list
data.append("jajuang")
print(f"data di Tambah lagi {data}")

#menambahkan list dengan list
data_baru = ["yujeng","Aseps","dangdeang"]
data.extend(data_baru)
print(f"data gabungan {data}")

#merubah dara 
# ubah data 2 menjadi walie
data[2] = "walie"
print(f"dara rubah = \n {data}")

#menghapus data 
data.remove("yujeng") # kalo data tidak di temukan akan eror karana data harus benar2 sesuai
print(f"Data Remove = \n {data}")

# meromve data paling belakang 
data.pop()
print(f"data akhir = {data}")

data_akhir =  data.pop()
print(f"data pop() {data_akhir}")






