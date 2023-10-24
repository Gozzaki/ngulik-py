#merubah tipe data ke tipe yg lain


#integer
print("=====integer======")
print("merubah data integer ke tipe data lain nya")
data_int = 0

print("data =",data_int,"type =", type(data_int))

data_str = str(data_int)
data_float = float(data_int)
data_bool = bool(data_int) #Akan True Jika Data INT Selain = 0

print("data =",data_str,"type =", type(data_str))
print("data =",data_float,"type =", type(data_float))
print("data =",data_bool,"type =", type(data_bool))

print("=====Float======")
print("merubah data Float ke tipe data lain nya")

data_float = 10.0

print("data =",data_float,"type =", type(data_float))

data_str = str(data_float)
data_int = int(data_float)
data_bool = bool(data_float) #Selain Data float = 0.0 bolean akan True

print("data =",data_str,"type =", type(data_str))
print("data =",data_int,"type =", type(data_int))
print("data =",data_bool,"type =", type(data_bool))

print("=====bolean======")
print("merubah data bolean ke tipe data lain nya")

data_bool = True

print("data =",data_bool,"type =", type(data_bool))

data_str =  str(data_bool) #akan berubah menjadi string "false"
data_int =  int(data_bool) #akan berubah menjadi int = 0 jika data bool = false. jika True data int = 1
data_float = float(data_bool) #akan berubah menjadi float = 0.0 jika data bool = false.  jika True data Float = 1.0

print("data =",data_str,"type =", type(data_str))
print("data =",data_int,"type =", type(data_int))
print("data =",data_float,"type =", type(data_float))

print("=====string======")
print("merubah data string ke tipe data lain nya")

data_string = "gozali"

print("data =",data_string,"type =", type(data_string))

data_bool =  bool(data_string) # Akan false jika data String di kosongkan
# data_int =  int(data_string)  #akan eror jika data String bukan angka
# data_float = float(data_string)

print("data =",data_bool,"type =", type(data_bool))
# print("data =",data_int,"type =", type(data_int))
# print("data =",data_float,"type =", type(data_float))
