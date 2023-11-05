
import datetime
import os

mahasiswa_template = {
    'nama' : 'gozali',
    'nim'  : '21416255201215' ,
    'sks_lulus' : 21,
    'lahir' : datetime.datetime(2003,6,17)
}

os.system("cls")
data_mahasiswa = {}
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print(f"{'-'*20:^20}")

mahasiswa = dict.fromkeys(mahasiswa_template.keys()) #membuat dictionary dengan mengambil keys dari template
print(mahasiswa)
mahasiswa['nama']= input("masukan nama :")
mahasiswa['nim']= input("masukan nim :")
mahasiswa['sks_lulus']= int(input("masukan sks lulus :"))
TAHUN_LAHIR= int(input("Tahun lahir (YYYY) :"))
BULAN_LAHIR= int(input("Bulan  lahir (1-12) :"))
TANGGAL_LAHIR= int(input("Tahun lahir (1-31) :" ))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(mahasiswa)

