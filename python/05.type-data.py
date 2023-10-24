#type data yg ada di python

# Tipe Data : Angka Satuan (integer)
data_integer =1
print("Data :",data_integer,"bertipe :" , type(data_integer))

#Tipe Data : Angka dengan koma (float)
data_float = 1.5
print("Data :",data_float,"bertipe :" , type(data_float))

#Tipe Data : Kumpulan Karakter (String)
data_string = "gozali"
print("Data :",data_float,"bertipe :" , type(data_string))

#Tipe Data : Biner True/False (boolean)
data_bool = False  
print("Data :",data_bool,"bertipe :" , type(data_bool))

##Tipe Data Khusus 

#bilangan Kompleks
data_complex = complex(5,1)

#Tipe Data dari bahasa C

from ctypes import c_double

data_c_doubel = c_double(10.5)
print("Data :",data_c_doubel,"bertipe :" , type(data_c_doubel))
