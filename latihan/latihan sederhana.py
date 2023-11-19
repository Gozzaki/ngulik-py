print("------STRUK BELANJA------")

print("-----------------------")
print("---List Harga Barang---")
print("-----------------------")
barang1 = input("Nama barang : ")
harga1 = input("Harga barang : ")

barang2 = input("Nama barang : ")
harga2 = input("Harga barang : ")

barang3 = input("Nama barang : ")
harga3 = input("Harga barang : ")

barang4 = input("Nama barang : ")
harga4 = input("Harga barang : ")

print("-------------------------------")
print("---Jumlah dan Harga Barang---")
print("-------------------------------")
jumlah1 = input(f"{barang1} x ")
print("=", int(jumlah1) * int(harga1))

jumlah2 = input(f"{barang2} x ")
print("=", int(jumlah2) * int(harga2))

jumlah3 = input(f"{barang3} x ")
print("=", int(jumlah3) * int(harga3))

jumlah4 = input(f"{barang4} x ")
print("=", int(jumlah4) * int(harga4))

print("-------------------------")
print("---Total Harga Barang---")
print("-------------------------")
hasil1 = (int(jumlah1) * int(harga1))
hasil2 = (int(jumlah2) * int(harga2))
hasil3 = (int(jumlah3) * int(harga3))
hasil4 = (int(jumlah4) * int(harga4))

total = (int(hasil1) + int(hasil2) + int(hasil3) + int(hasil4))
print("Total harga = ", total)
print("-----------------")

print("-----------------")
print("!!! Diskon 10% !!!")
print("-----------------")
diskon = (total * 10) / 100
print("TOTAL = ", total - diskon)