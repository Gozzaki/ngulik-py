#latihan perulangan membuat segitiga


sisi = 10

# 1. menggunakan while
#dummmy variabel

print("awal Dari For")  
count = 1
for i in range(4):
    print("*"*count)
    count +=1
print("akhir Dari For\n")  
    
# 2. Menggunakan wihle 
print("awal dari while")
count = 1
while True:
    print("*"*count)
    count +=1

    if count > sisi:
        break
print("akhir dari while\n")

# 3. Menggunakan wihle 
print("while ganjil")
count = 1
spasi = int(sisi / 2)
while True:
    if count > sisi:
        break
    
    if count % 2 != 0 : 
        print(" "*spasi,"0"*count)
        count +=1
        spasi -=1
        continue
    else:
        #akan kembali ke atas jika ganjil
        count +=1
        continue


sisi = int(input("Masukan panjang sisi :"))
panjang = 1
count = 1
while True:

    if (count < sisi):
        print((panjang*"*").center(sisi+1))
        count += 2
        panjang += 2
    else:
        print((panjang*"*").center(sisi+1))
        panjang -= 2
    
    if panjang < 1:
        break
print("akhir dari while ganjil")


