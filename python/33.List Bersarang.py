data_0 = [ 1,2]
data_1 = [3,4,]
data_list_biasa = [1,2,3,4]
print(f" list biasa = {data_list_biasa}")

list_2D = [data_0,data_1]
print(f" list 2D = {list_2D}")

#contoh pengguanaa 
peserta_0 = ["gozali",20,"laki-laki"]
peserta_1 = ["zakia",20,"perempuan"]
peserta_2 = ["gozzaki",18,"laki-laki"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")

# dengan reference

list_copy = list_peserta.copy()
print(f"peserta = {list_copy}")
peserta_2[0] = "lielie"
print(f"peserta = {list_copy}\n")
print(f"peserta = {list_peserta}")
