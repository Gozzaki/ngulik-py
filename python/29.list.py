#LIST (kumpulan data)

# Kumpalan data numbers
angka = [1,2,3]
print(angka)

#kumpulan data stirng
string = ["ali","gozzaki","jay"]
print(string)

#kumpulan data bolean 
bolean = [True,False,True]
print(bolean)

#kumpulan campuran
data_campuran = [ 1,"gehu",True,2,"bala-bala",False]
print(data_campuran)

## Cara alternatif membuat list
data_range = range(0,10,2) #range(star,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

#membuat list dengan for loop,list comprehension
list_pake_for = [i*5 for i in range(0,10)]
print(list_pake_for)

list_for_if = [i for i in range(0,10) if i !=5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 ==0] #membuat List Genap Menggunakan for if
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 !=0] #membuat List Ganjil Menggunakan for if
print(list_for_if)