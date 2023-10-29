data_angka = [1,1,2,3,5,6,9,8,7,7,1,7]
print  (f"data angka = \n{data_angka}")

#count(data dalam list) akan menghitung jumlah data tersebut pada list


jumlah_data_4 = data_angka.count(4)  #mengghitung jumlah data 4 pada list
jumlah_data_7 = data_angka.count(7)  

print(f"jumlah angka 4 =  {jumlah_data_4}")
print(f"jumlah angka 7 =  {jumlah_data_7}")

#index("kia") untuk melihat index "kia" pada list

data = [ "jayal","gozzaki" ,"kia"]
print(f" data = {data}")

index_kia = data.index("kia") # cara mengetahui/mengambil no index

print(f"index kia adalah = {index_kia}")

#mengurutkan list 
print(f" data angka sebelum di sort = \n {data_angka}")
data_angka.sort()  #mengurutkan data  Ascending (Meningkat):
print(f"data angka sort = \n {data_angka} ")

#string  
print(f"data = {data}")
data.sort()
print(f"data short = {data}")

#balik listnya  Descending (Menurun):
data_angka.reverse()
data.reverse()
print(f" data rivers = \n{data_angka} \n {data} ")




