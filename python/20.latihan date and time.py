# date and time (latihan)

import datetime as dt

# hari_ini = dt.date.today()
# print(hari_ini)

# tanggal = dt.date(2003,6,10)
# print(tanggal)
# print(f"Hari Ini adalah hari = {tanggal:%A}") # %A untuk merubah output tanggal (2003-06-10) menjadi hari (Tuesday)

# print("Silajkan <Asukan Tanggal ,\nBulan Dan Tahun lahir anda")
# tanggal =  int(input("tanggal\t:"))
# bulan =  int(input("Bulan\t:"))
# tahun =  int(input("Tahun\t:"))

# tanggal_lahir = dt.date(tahun,bulan,tanggal)
# print(f"Tanggal Lahir Anda Adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
tanggal = 17
bulan = 6
tahun = 2003
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"har ini tanggal : {hari_ini}")
print(f"tanggal lahir anda: {tanggal_lahir}")
umur_hari = hari_ini - tanggal_lahir 
print(umur_hari)
umur_tahun = umur_hari.days // 360
umur_bulan = (umur_hari.days % 365)  // 30

print(f"umur anda adalah : {umur_tahun} Tahun  {umur_bulan} Bulan")
print(f"Hari nya Adalah : {tanggal_lahir:%A}")




