#looping dari list 

#forr loop
print(" For Loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["gozali","gozzaki","zakia"]

for nama in peserta:
    print(f"nama = {nama}")


# for loop dan range
print(" For Loop dan range")
kumpulan_angka = [10,5,4,2,6]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")


#while 
print(" while loop")

kumpulan_angka = [10,5,4,2,6]

panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1
#list comprehension 
print(" list comprehension")

data = ["gozali",1,2,3,"zakia"]

[print(f"data = {i}") for i in data]

angka = [1,2,3,4,5]

angka_kuadrat = [i**5 for i in angka]
print(f"{angka_kuadrat}")

# enumerete
print(" enumerete")
data = ["gozali",1,2,3,"zakia"]

for index,data in enumerate(data):
    print(f"index = {index},data = {data}")
