'''Ltihan Fungsi '''

import os
#program menghitung luas dan keliling persegi 

#membuat header 
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user

# PANJANG = int(input("Masukan Nilai Panjang : "))
# LEBAR = int(input("Masukan Nilai Lebar : "))

# # Program Menghitung luas  
# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # tampilkan hasil
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan Keliling  = {KELILING}")

def header():
    '''Fungsi Header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

while True:
    header()
    isContinue = input("apakah lanjut (Y/N)").upper()
    if isContinue == "N":
        break

def input_user():
    panjang = int(input("Masukan Nilai Panjang : "))
    lebar  = int(input("Masukan Nilai Lebar : "))

print("Program Selesai TerimaKasih")
