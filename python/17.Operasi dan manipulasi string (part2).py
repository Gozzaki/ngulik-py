# operasi dalam bentuk method

## merubah case dari sting 

# merubah semua ke upper case 

salam = "bro!"

print("normal  = " + salam)
salam = salam.upper() #merubah isi variabel salam menjadi huruf kapital
print("upper  = " + salam)

#merubah semua ke lower case 
alay = "Aku KeCe AbiesZZZzzz"
print("normal  = " + salam)
salam = salam.lower() # merubah isi variabel salam menjadi huruf kecil 
print("lower  = " + salam)

## pengecekan dengan isX method

#contoh pengecekan lower case 
salam = "sist"
apakah_lower = salam.islower() #hasilnya bolean # mengecek varibael salam apakah lower
print(salam + "is lower = " + str(apakah_lower))
apakah_lower = salam.isupper() # mengecek variabel salam apakah upper
print(salam + "is upper = " + str(apakah_lower))

# isalpha() <-- untuk mengecek semuanuya huruf 
# islnum() <-- huruf dan angka 
# isdecimal() <-- angka saja
# isspace()  <-- spasi ,tab ,newline 
# istitle <-- semua kata dengan huruf besar 

judul = "It Is Okay Not To Be Orkay"
cek_judul =  judul.istitle() #hasilnya bolean 
print(judul + " title ini = " +str(cek_judul))

judul = "It is Okay Not To be Orkay".title()
#cek_judul =  judul.title()  # merubah variabel judul menajadi title 
print(judul + " title ini = ") #str(cek_judul))

## mengecek komponen startswicth() endswith 

cek_start = "Sangjamnim Opaa".startswith("Sangjamnim")
print("start = " + str(cek_start))

cek_end = "Sangjamnim Opaa".endswith("Opaaa")

## menggabukna komponen join() split()

#menggabukan data list jadi satu
pisah = ["aku","sayang","zakia"]
gabungan = '.'.join(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' hem '.join(pisah)
print(gabungan)

#membuat data menjadi list
gabungan = "akuhemsayanghemzakia"
print(gabungan.split("hem"))

#alokasi karakter  rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kanan+"'")

tengah = "tengah".center(15,":")
print("'"+tengah+"'")

# ebalikan nya -> strip()
tengah = tengah.strip(":") #menghilangkan tadan :
print("'"+tengah+"'")

kanan = kanan.strip()
print()





