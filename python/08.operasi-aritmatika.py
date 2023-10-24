a = 5
b = 3

#Operasi Tambah (+)
hasil = a + b 
print(a ,"+", b ,"=", hasil)

#Operasi Pengurangan  (-)
hasil = a - b 
print(a ,"+", b ,"=", hasil)

#Operasi Kali (*)
hasil = a * b 
print(a ,"x", b ,"=", hasil)

#Operasi Pembagian (/)
hasil = a / b 
print(a ,"/", b ,"=", hasil)

#Operasi eksponen (Pangkat) **
hasil = a ** b 
print(a ,"pangkat", b ,"=", hasil)

#Operasi Modulus (Sisa Pembagian) %
hasil = a % b 
print(a ,"Modulus", b ,"=", hasil)

#Operasi Flor Division (//)
hasil = a // b 
# print(a ,"pangkat", b ,"=", hasil)

#Prioritas Operasi

'''
    1> ()
    2. eksponen 
    3. Perkalian dan Teman - Teman  * / ** % //
    4. Pertambahan Dan Pengurangan  + -

'''
x = 2
y = 3
z = 4

hasil = x ** y * z + x / y - y % z // x
print( x,"**", y ,"*" ,z, "+" ,x ,"/",y ,"-" ,y ,"%" ,z ,"//" ,x ,"=",hasil)

hasil =  x + y * z
print(x ,"+", y, "*", z , '=', hasil)

#Kurung Akan Mengambil Langkah Paling Pertama 
hasil = (x + y) * z
print('(',x ,"+", y,")", "*", z, '=', hasil)
