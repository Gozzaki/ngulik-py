#break

#break statement untuk menghentikan perulangan

angka = 0
while angka < 5:
    angka += 1
    print(f"angka Sekarang adalah {angka}")

    if angka == 3 :
        print("niceee")
        break

    print("wasup")

#----------------------------------
data_int = int(input("hitung angka sampe brp?"))
angka = 0
while True:
    angka += 1
    print(f"angka Sekarang adalah {angka}")

    if angka == data_int :
        print("niceee")
        break

    print("wasup")

