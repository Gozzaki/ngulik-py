data_0 = [1,"x"]
data_1 = [0,"y"]

data_2D = [data_0,data_1 , 15]
data_2D_copy = data_2D.copy()  #tidak merubah address list di yang ada di dalam list
print(f"data = {data_2D}")
print(f"data  copy = {data_2D_copy}")


#mengambil data  dari nested list (list dalam list)

data = data_2D[1][0]
print(f"data = {data}")

#address semuanya 
print(f"address asli = {hex(id(data_2D))}")
print(f"address asli = {hex(id(data_2D_copy))}")

print(f"address member ke -1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address asli = {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5  #data asli dan copy akan berubah
data_2D [2] = 7
print(f"data = {data_2D}")
print(f"data = {data_2D_copy}")

#kita gunakan deepcopy 

from copy import deepcopy
data_2D = [data_0,data_1 , 15]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address member ke -1 deepcopy ")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address asli = {hex(id(data_2D_deepcopy[0]))}")

data_2D [0][1] = 30
print(f"data = {data_2D}")
print(f"data deepcopy= {data_2D_deepcopy}")









