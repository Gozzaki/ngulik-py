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

def input_user():
    '''Fungsi Input User'''
    panjang = int(input("Masukan Nilai Panjang : "))
    lebar  = int(input("Masukan Nilai Lebar : "))
    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''Fungsi Luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)

def display(massege,value):
    print(f"hasil perhitungan {massege} = {value }")
while True:
    header()

    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display("luas",LUAS)
    display("Keliling",KELILING)

    isContinue = input("apakah lanjut (Y/N)").upper()
    if isContinue == "N":
        break
    
print("Program Selesai TerimaKasih")
