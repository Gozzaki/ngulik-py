
import datetime
import os
import string
import random

mahasiswa_template = {
    'nama' : 'gozali',
    'nim'  : '21416255201215' ,
    'sks_lulus' : 21,
    'lahir' : datetime.datetime(2003,6,17)
}
data_mahasiswa = {}
while True:
    os.system("cls")
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

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})
    print(f"\n{'KEY':<6} {'nama':<17} {'nim':<6} {'SKS':<5} {'lahir':<10}")

    for i in data_mahasiswa:
        KEY = i
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        print(f"{KEY:<6} {NAMA:<17} {NIM:<6} {SKS:<5} {LAHIR:<10}")

    print("\n")
    is_done = input("Mau Tambah Lagi BRO (y/n)")
    if is_done == "n":
        break

print("terima kasih")
