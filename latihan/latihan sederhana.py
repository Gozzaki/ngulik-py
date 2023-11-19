print("------STRUK BELANJA------")
print("-----------------------")
print("---List Harga Barang---")
print("-----------------------")

# Meminta input jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Inisialisasi list untuk menyimpan nama dan harga barang
daftar_barang = []
daftar_harga = []

# Menggunakan loop untuk mendapatkan input untuk setiap barang
for i in range(jumlah_barang):
    nama_barang = input(f"Nama barang {i + 1}: ")
    harga_barang = float(input(f"Harga barang {i + 1}: "))
    daftar_barang.append(nama_barang)
    daftar_harga.append(harga_barang)

print("-------------------------------")
print("---Jumlah dan Harga Barang---")
print("-------------------------------")

# Inisialisasi total harga
total_harga_semua_barang = 0

# Menggunakan loop untuk mencetak jumlah dan harga setiap barang
for i in range(jumlah_barang):
    jumlah = int(input(f"{daftar_barang[i]} x "))
    total_harga_barang = jumlah * daftar_harga[i]
    print("=", total_harga_barang)
    total_harga_semua_barang += total_harga_barang

print("-------------------------")
print("---Total Harga Barang---")
print("-------------------------")

print("Total harga =", total_harga_semua_barang)
print("-----------------")

print("-----------------")
print("!!! Diskon 10% !!!")
print("-----------------")

# Menghitung dan mencetak total harga setelah diskon
diskon = total_harga_semua_barang * 0.1
total_setelah_diskon = total_harga_semua_barang - diskon
print("TOTAL =", total_setelah_diskon)
