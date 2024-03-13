# Project Pemrograman Dasar Praktikum #

# Membuat Aplikasi Traveler



import os

#___________________________________________________________________Tabel Paket________________________________________________________________________________#

# Kolom Kode Paket

kolom_kode_paket = ["01", "02", "03", "04"]

kolom_rute_perjalanan   =   ["Karawang - Pantai Pakis Jaya", "Karawang - Curug Cigentis - Gunung Sangga Buana",
                            "Karawang - Candi Jiwa", "Karawang - Pantai Samudra", ]

kolom_min_peserta = ["6 Orang", "6 Orang", "4 Orang", "5 Orang"]

kolom_harga_perjalanan   =  ["Rp. 1.000.000",
                            "Rp. 500.000", "Rp. 600.000", "Rp. 850.000"]

kolom_harga_perjalanan_int = [1_000_000, 500_000, 600_000, 850_000]

# Kolom Kode Tambahan

kolom_paket_tambahan = ["A", "B", "C"]

kolom_fasilitas = ["Penginapan", "Penjemputan", "Kuliner"]

kolom_harga_tambahan = ["Rp. 600.000", "Rp. 300.000", "Rp. 300.000"]

kolom_harga_tambahan_int = [600_000, 300_000, 300_000]

#_____________________________________________________________________________________________________________________________________________________________#

# Fungsi List Menu Kode Paket

def show_kode_paket_perjalanan():

    print("}"f"------------------------------ DAFTAR KODE PAKET ------------------------------""{")

    print(f"\n[ KODE ] RUTE PERJALANAN / MINIMUM PESERTA / TARIF\n")

    for pilihan_paket_tujuan in range(len(kolom_kode_paket)):

        print(f"[  {(kolom_kode_paket)[pilihan_paket_tujuan]}  ] {(kolom_rute_perjalanan)[pilihan_paket_tujuan]} / {(kolom_min_peserta)[pilihan_paket_tujuan]} / {(kolom_harga_perjalanan)[pilihan_paket_tujuan]}")

# Fungsi List Menu Kode Tambahan

def show_fasilitas_tambahan():

    print("\n}"f"----- DAFTAR KODE TAMBAHAN -----""{")
    print(f"\n[ KODE ] FASILITAS / TARIF\n")

    for pilihan_fasilitas_tambahan in range(len(kolom_paket_tambahan)):

        print(f"[  {kolom_paket_tambahan[pilihan_fasilitas_tambahan]}   ] {kolom_fasilitas[pilihan_fasilitas_tambahan]} / {kolom_harga_tambahan[pilihan_fasilitas_tambahan]}")

# Tambah Peserta

def peserta_TAMBAH():

    os.system("cls")

    show_kode_paket_perjalanan()

    show_fasilitas_tambahan()

    # input nama peserta

    while True:

        nama_peserta = input("\nNama Peserta\t\t:\t")

        kode_paket = input("Kode Paket\t\t:\t")

        match kode_paket:

            case "01":

                # Harga Perjalanan & Rute Perjalanan

                tarif_perjalanan, rute_perjalanan = kolom_harga_perjalanan_int[
                    0], kolom_rute_perjalanan[0]

                print(
                    f"Nama Paket\t\t:\t{kolom_rute_perjalanan[0]} / {kolom_min_peserta[0]}")

                print(f"Tarif Paket\t\t:\t{kolom_harga_perjalanan[0]}")

                break

            case "02":

                # Harga Perjalanan & Rute Perjalanan

                tarif_perjalanan, rute_perjalanan = kolom_harga_perjalanan_int[
                    1], kolom_rute_perjalanan[1]

                print(
                    f"Nama Paket\t\t:\t{kolom_rute_perjalanan[1]} / {kolom_min_peserta[1]}")

                print(f"Tarif Paket\t\t:\t{kolom_harga_perjalanan[1]}")

                break

            case "03":

                # Harga Perjalanan & Rute Perjalanan

                tarif_perjalanan, rute_perjalanan = kolom_harga_perjalanan_int[
                    2], kolom_rute_perjalanan[2]

                print(
                    f"Nama Paket\t\t:\t{kolom_rute_perjalanan[2]} / {kolom_min_peserta[2]}")

                print(f"Tarif Paket\t\t:\t{kolom_harga_perjalanan[2]}")

                break

            case "04":

                # Harga Perjalanan & Rute Perjalanan

                tarif_perjalanan, rute_perjalanan = kolom_harga_perjalanan_int[
                    3], kolom_rute_perjalanan[3]

                print(
                    f"Nama Paket\t\t:\t{kolom_rute_perjalanan[3]} / {kolom_min_peserta[3]}")

                print(f"Tarif Paket\t\t:\t{kolom_harga_perjalanan[3]}")

                break

    # input kode tambahan

    while True:

        kode_tambahan = input(f"Kode Tambahan\t\t:\t").upper()
        
        print(kode_tambahan)
        match kode_tambahan:

            case "A":
                # Harga Tambahan & Fasilitas
                tarif_tambahan, fasilitas = kolom_harga_tambahan_int[0], kolom_fasilitas[0]

                print(f"Fasilitas\t\t:\t{kolom_fasilitas[0]}")

                print(f"Tarif Tambahan\t\t:\t{kolom_harga_tambahan[0]}")

                break

            case "B":

                # Harga Tambahan & Fasilitas

                tarif_tambahan, fasilitas = kolom_harga_tambahan_int[1], kolom_fasilitas[1]

                print(f"Fasilitas\t\t:\t{kolom_fasilitas[1]}")

                print(f"Tarif Tambahan\t\t:\t{kolom_harga_tambahan[1]}")

                break

            case "C":

                # Harga Tambahan & Fasilitas

                tarif_tambahan, fasilitas = kolom_harga_tambahan_int[2], kolom_fasilitas[2]

                print(f"Fasilitas\t\t:\t{kolom_fasilitas[2]}")

                print(f"Tarif Tambahan\t\t:\t{kolom_harga_tambahan[2]}")

                break

    #_________________________________________________________Kalkulasi________________________________________________________________#

    jumlah_tarif = tarif_perjalanan + tarif_tambahan

    print(f"Total Tarif\t\t:\tRp. {jumlah_tarif:,} ")

    # PPN 11%

    harga_ppn = (jumlah_tarif * 11) / 100

    print(f"PPN (11%)\t\t:\tRp. {harga_ppn:,} ")

    # Total Bayar

    jumlah_bayar = jumlah_tarif + harga_ppn

    print(f"Jumlah Biaya\t\t:\tRp. {jumlah_bayar:,} ")

    # Store Data

    data = f"{nama_peserta} / {rute_perjalanan} / {fasilitas} / Rp. {jumlah_bayar:,} ]"

    with open("DataTransaksi.txt", "a") as f:

        f.write(str(data) + "\n")

    print(f"\nData Berhasil Disimpan")

    f.close()

    interaksi()

    #__________________________________________________________________________________________________________________________________#

# Lihat Peserta

def peserta_LIHAT():

    os.system("cls")

    print("}"f"------------------------------ LIHAT PESERTA ------------------------------""{")

    show_peserta()

    interaksi()

# Fungsi Menghapus Data Peserta

def peserta_HAPUS():

    os.system("cls")

    print("}"f"------------------------------ HAPUS PESERTA ------------------------------""{")

    show_peserta()

    with open("DataTransaksi.txt", "r") as f:

        jml_baris = sum(1 for line in f)

    #  Pilih Nomor Peserta

    hapus_nomor = int(input(f"\n$No. Peserta >> "))

    if hapus_nomor - 1 not in range(jml_baris):

        print(f"Peserta Tidak Ada")

        interaksi()

    else:

        # menghapus data peserta

        with open("DataTransaksi.txt", "r") as f:

            baris = f.readlines()

            baris.pop(hapus_nomor - 1)

        # Menulis kembali file

        with open("DataTransaksi.txt", "w") as f:

            for data in baris:

                f.write(data)

    print(f"\nData Berhasil Dihapus")

    f.close()

    interaksi()

# Fungsi Cari Peserta

def peserta_CARI():

    os.system("cls")

    print("}"f"------------------------------ CARI PESERTA ------------------------------""{")

    # Membuat Variabel Data Peserta 

    with open("DataTransaksi.txt", "r") as f:

        data_transaksi = f.readlines()

    while True:

        nama_peserta = input(f"\n$Nama Peserta >> ")

        if nama_peserta == "":

            print(f"Nama Pesqerta Tidak Boleh Kosong")

            interaksi()

        else:

            break

    print("\n}"f"----- HASIL PENCARIAN -----""{\n")

    for index in range(len(data_transaksi)):

        if nama_peserta + " " in data_transaksi[index]:

            print(f"[  {index+1}  ][ {data_transaksi[index]}")

    interaksi()

# Fungsi Menampilkan Data Peserta

def show_peserta():

    # Variabel Data Peserta

    with open("DataTransaksi.txt", "r") as f:

        data_transaksi = f.readlines()

    with open("DataTransaksi.txt", "r") as f:

        jml_peserta = sum(1 for line in f)
    
    print(f"\n[ No. ][ Nama Peserta / Paket / Tambahan / Total Bayar ]\n")

    # Hasil
    for index in range(jml_peserta):

        print(f"[  {index+1}  ][ {data_transaksi[index]}")

    return jml_peserta, data_transaksi

# Interaksi Akhir

def interaksi():

    input("\nTekan Enter Untuk Kembali..")

    os.system("cls")

    menu()

# Fungsi Menu

def menu():

    menu = 5

    while True:

        try:

            print(f'''
        

''')

            print("\t}"f"---------------------------------------------""{")
            print("}"f"------------------- TIKET TRAVELER ---------------------""{")
            print("\t}"f"---------------------------------------------""{\n")

            print(f"\t[ 1 ] Tambah Transaksi Peserta")
            print(f"\t[ 2 ] Lihat Daftar Peserta")
            print(f"\t[ 3 ] Hapus Peserta")
            print(f"\t[ 4 ] Cari Peserta")
            print(f"\t[ 5 ] Exit")

            pilih = int(input(f"\n\t$Pilih Menu >> "))

            if pilih > menu or pilih < 1:

                print(f"\n! Menu Tidak Ada !")

                continue

            # Metode Dictionary

            selecting_menu = {

                1: peserta_TAMBAH,

                2: peserta_LIHAT,

                3: peserta_HAPUS,

                4: peserta_CARI,

                5: exit

            }

            # Metode get() untuk mengambil nilai dari dictionary

            return selecting_menu.get(int(pilih))()

        except ValueError:

            print(f"\n! Menu Tidak Ada !")

            continue

if __name__ == '__main__':

    menu()
