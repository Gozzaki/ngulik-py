
#perulangan (loop)

# ini dengan list
angka2_list = [1,2,3,4,5,5,4,3,2,1]
print(angka2_list)

for i in angka2_list:
    print(f" i sekarang: {i}")


print("selesai 1\n")

#ini dengan range
angka2_range = range(5) #output akan looping 0 sampai 4 

for i in angka2_range:
    print(f" i sekarang: {i}")

print("selesai 2\n")

angka2_range = range(1,5) #uotput akan looping 1 sampai 4

for i in angka2_range:
    print(f" i sekarang: {i}")

print("selesai 3\n")

#menggunakan string 

data_str = "Saya mengulik py" #output akan looping per satu huruf
for i in data_str:
    print(i)
print("selesai 3\n")









