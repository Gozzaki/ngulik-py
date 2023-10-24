#operasi dan manipulasi string
# 1. menyambung stinr 
nama_pertama = "gojay"
nama_tengah = "lie"
nama_akhir = "atamimi"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

#2. menghitung panjang sting
panjang = len(nama_lengkap)
print("panjang dari" + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string 

# mengecek apakah ada kompnen char atau sting di string

d = "gozali"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

#kebalikan dari in
d = "gozali"
status = d not in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

#mengulang string
print("wk"*10)

print(15*"wk")

#indexing melihat char sesuai index
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1]) # diamblil dari belakang
print("index ke-[0-6] : " + nama_lengkap[0:6]) # : adalah sampai 
print("index ke-[0-6] : " + nama_lengkap[6:9]) # : adalah sampai 
print("index ke-[0-6] : " + nama_lengkap[0:9:2]) # dilangkah 2 

# item paling kecil 
print("paling kecil :" + min(nama_lengkap))
print("paling besar :" + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117 
print("char untuk ASCII 117 adalah " + chr(data))

# 4.opeeator dalam bentuk metod

data = "yog tong otong "
jumlah = data.count("o")
print("jumlah o pada " + data + "=" + str(jumlah))
