# continue ,pass , break

# pass -> dia berfungsi sebagai dummy , tidak akan di eksekusi
angka = 0

while angka < 5:
    angka += 1
    if angka == 3:
        pass
    print(f"angka Sekarang adalah {angka} dan gozali kece")

#--------------------------------------------

# continue -> dia akan menghentikan aksi yang sedang berjalan , lalu melanjutkan ke aksi selanjutnya
angka = 0

while angka < 5:
    angka += 1
    if angka == 3:
        print("angka Sekarang adalah", angka)
        continue # akan membuat loop meloncat ke step selanjutnya
    print(f"angka Sekarang adalah {angka} dan gozali kece")