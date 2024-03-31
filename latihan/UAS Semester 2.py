
from colorama import Fore
import os

#untuk menampilkan menu
def show_daftar():
    print("}"f"--------------------- PD. Travekar ------------------------""{")
    print("}"f"---------- Paket Wisata dan Layanan Yang Tersedia ----------""{\n")

    print(f"""   
:----------------------------------------------------------------------:
|kode paket|     rute perjalanan     | Minimum perserta | tarif        |
|----------+-------------------------+------------------+--------------|
|    01    |karawang - Pantai Pakis  |      6 orang     | Rp.1.000.000 |
|    02    |Karawang - Curug Cigentis|      6 Orang     | Rp.500.00    |
|    03    |Karawang - candi Jiwa    |      4 Orang     | Rp.600.00    |
|    04    |Karawang - Pantai Sadari |      5 Orang     | Rp.850.00    |
:----------------------------------------------------------------------:\n
Layanan Tmabahan Yang Dapat Ditambahkan :
:--------------------------------------:
|Kode Tambahan| Fasilitas  | tarif     |
|--------------------------------------|
|      A      | Penginapan | Rp.600.000|
|      B      | Penjemputan| Rp.300.000|
|      C      | Kuliner    | Rp.300.000|
:--------------------------------------:
""")

def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return 'Rp ' + y     
    else :
        p = y[-3:]
        q = y[:-3]
        return   formatrupiah(q) + '.' + p
        print('Rp ' +  formatrupiah(q) + '.' + p)
data = []
pembayaran = {}

def tambah_data():
    show_daftar()
    peserta = str(input("Masukan Nama : "))
    paket = str(input("Masukan Kode Paket : "))
    print(f"Nama \t\t\t:\t{peserta} ")
    #_________________________________________________________PERULANGAN UNTUK OUTPUT___________________________________________________________________#
    match paket:

            case "01":
                print(f"Nama Paket\t\t:\tKarawang - Pantai Pakis")
                print(f"Tarif Paket\t\t:\tRp.1.000.00")  
                
            case "02":
                print(f"Nama Paket\t\t:\tKarawang - Curug Cigentis")
                print(f"Tarif Paket\t\t:\tRp.500.000")

            case "03":
                print(f"Nama Paket\t\t:\tKarawang - Candi Jiwa")
                print(f"Tarif Paket\t\t:\tRp.600.000")


            case "04":
                print(f"Nama Paket\t\t:\tkarawang - Pantai Sadari")
                print(f"Tarif Paket\t\t:\tRp.850.000")

    layanan = str(input("Kode Tambahan\t\t:\t"))
    #__________________________________________________________________ PERULANGAN UNTUK MENGUMPULAN DATA______________________________________________________________________#
    if paket == "01" and layanan.upper() == "A":
        harga_paket =   1000000
        harga_layanan = 600000 
        jumlah_tarif = harga_paket + harga_layanan     
        harga_ppn = int((jumlah_tarif * 11) / 100 )                             
        data_tambahan = f"{peserta}    | Karawang - Pantai Pakis  | {formatrupiah(harga_paket)} |     Penginapan      | {formatrupiah(harga_layanan)}       |"
        data.append(data_tambahan)     #{formatrupiah(jumlah_tarif + harga_ppn)}
        pembayaran.update({f"{peserta}":f"{peserta} | Karawang - Pantai Pakis |     Penginapan      | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    elif paket == "01" and layanan.upper() == "B":
        harga_paket = 1000000
        harga_layanan = 300000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = int((jumlah_tarif * 11) / 100 )
        data_tambahan = f"{peserta}    | Karawang - Pantai Pakis  | {formatrupiah(harga_paket)} |     Penjemputan     | {formatrupiah(harga_layanan)}       |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | Karawang - Pantai Pakis |     Penjemputan     | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    elif paket == "01" and layanan.upper() == "C":
        harga_paket = 1000000
        harga_layanan = 300000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = int((jumlah_tarif * 11) / 100 )
        data_tambahan = f"{peserta}    | Karawang - Pantai Pakis  | {formatrupiah(harga_paket)} |      Kuliner        | {formatrupiah(harga_layanan)}       |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | Karawang - Pantai Pakis |      Kuliner        | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    # jika paket 02
    elif paket == "02" and layanan.upper() == "A":
        harga_paket = 500000
        harga_layanan = 600000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = int((jumlah_tarif * 11) / 100 )
        data_tambahan = f"{peserta}    |Karawang - Curug Cigentis | {formatrupiah(harga_paket)}   |     Penginapan     | {formatrupiah(harga_layanan)}        |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | Karawang - Curug Cigentis |     Penginapan     | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    elif paket == "02" and layanan.upper() == "B":
        harga_paket = 500000
        harga_layanan = 300000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = int((jumlah_tarif * 11) / 100 )
        data_tambahan = f"{peserta}    |Karawang - Curug Cigentis | {formatrupiah(harga_paket)}  |     Penjemputan     | {formatrupiah(harga_layanan)}        |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | Karawang - Curug Cigentis |     Penjemputan     | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    elif paket == "02" and layanan.upper() == "C":
        harga_paket = 500000   
        harga_layanan = 300000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = (jumlah_tarif * 11) / 100
        data_tambahan =f"{peserta}     | Karawang - Curug Cigentis | {formatrupiah(harga_paket)}  |      kuliner        | {formatrupiah(harga_layanan)}       |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | Karawang - Curug Cigentis |      kuliner        | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    #jika paket 03
    elif paket == "03" and layanan.upper() == "A":
        harga_paket = 600000
        harga_layanan = 600000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = int((jumlah_tarif * 11) / 100 )
        data_tambahan = f"{peserta}    |  Karawang - Candi Jiwa   | {formatrupiah(harga_paket)}  |      Penginapan     | {formatrupiah(harga_layanan)}        |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | Karawang - Candi Jiwa |      Penginapan     | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    elif paket == "03" and layanan.upper() == "B":
        harga_paket = 600000
        harga_layanan = 300000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = int((jumlah_tarif * 11) / 100 )
        data_tambahan = f"{peserta}    |  Karawang - Candi Jiwa   | {formatrupiah(harga_paket)}  |     Penjemputan     | {formatrupiah(harga_layanan)}        |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | Karawang - Candi Jiwa |     Penjemputan     | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    elif paket == "03" and layanan.upper() == "C":
        harga_paket = 600000
        harga_layanan = 300000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = int((jumlah_tarif * 11) / 100 )
        data_tambahan = f"{peserta}    |  Karawang - Candi Jiwa   | {formatrupiah(harga_paket)}  |       Kuliner       | {formatrupiah(harga_layanan)}        |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | Karawang - Candi Jiwa |       Kuliner       | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    #jika paket 04
    elif paket == "04" and layanan.upper() == "A":
        harga_paket = 850000
        harga_layanan = 600000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = int((jumlah_tarif * 11) / 100 )
        data_tambahan = f"{peserta}    | karawang - Pantai Sadari | {formatrupiah(harga_paket)}  |      Penginapan     | {formatrupiah(harga_layanan)}        |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | karawang - Pantai Sadari |      Penginapan     | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    elif paket == "04" and layanan.upper() == "B":
        harga_paket = 850000
        harga_layanan = 300000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = int((jumlah_tarif * 11) / 100 )
        data_tambahan = f"{peserta}    | Karawang - Pantai Sadari | {formatrupiah(harga_paket)}  |    Penjemputan      | {formatrupiah(harga_layanan)}        |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | karawang - Pantai Sadari |    Penjemputan      | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    elif paket == "04" and layanan.upper() == "C":
        harga_paket = 850000
        harga_layanan = 300000
        jumlah_tarif = harga_paket + harga_layanan
        harga_ppn = int((jumlah_tarif * 11) / 100 )
        data_tambahan = f"{peserta}    | Karawang - Pantai Sadari | {formatrupiah(harga_paket)}  |       kuliner       | {formatrupiah(harga_layanan)}        |"
        data.append(data_tambahan)
        pembayaran.update({peserta:f"{peserta} | karawang - Pantai Sadari |       kuliner       | {formatrupiah(jumlah_tarif + harga_ppn)} "})
    else:
        print("kode yang anda masukan salah")
    #_________________________________________________________PERULANGAN UNTUK OUTPUT___________________________________________________________________#

    # input kode tambahan

    match layanan:

            case "A":
                
                print(f"Fasilitas\t\t:\tPenginapan")

                print(f"Tarif Tambahan\t\t:\tRp.600.000")

                

            case "B":

                print(f"Fasilitas\t\t:\tPenjemputan")

                print(f"Tarif Tambahan\t\t:\tRp.300.000|")

                

            case "C":

                print(f"Fasilitas\t\t:\tKuliner")

                print(f"Tarif Tambahan\t\t:\tRp.300.000")

                

    #_________________________________________________________Kalkulasi________________________________________________________________#


    print(f"Total Tarif\t\t:\t{formatrupiah(jumlah_tarif)} ")

    # PPN 11%                   {formatrupiah(harga_ppn)}


    print(f"PPN (11%)\t\t:\t{formatrupiah(harga_ppn)} ")
   
    # Total Bayar

    jumlah_bayar = jumlah_tarif + harga_ppn

    print(f"Jumlah Biaya\t\t:\t{formatrupiah(jumlah_bayar)} ")
    print(f"\n{Fore.GREEN}Data Berhasil Disimpan{Fore.RESET}")
    interaksi()

def show_data():
    if len(data) <= 0:
        print("BELUM ADA DATA")
    else:
        
        
        print(":----------------------------------------------------------------------------------------------:")
        print("|NO|   Nama   |     Rute Perjalanan     | Harga paket  | fasilitas tambahan | Harga fasilitas  |")
        print(":----------------------------------------------------------------------------------------------:")
        
        for indeks in range(len(data)):
            print(f"|{indeks+1} | {data[indeks]}")
        print(":-----------------------------------------------------------------------------------------------:\n")
    interaksi()

def show_data2():
    if len(data) <= 0:
        print("BELUM ADA DATA")
    else:
        
        
        print(":----------------------------------------------------------------------------------------------:")
        print("|NO|   Nama   |     Rute Perjalanan     | Harga paket  | fasilitas tambahan | Harga fasilitas  |")
        print(":----------------------------------------------------------------------------------------------:")
        
        for indeks in range(len(data)):
            print(f"|{indeks+1} | {data[indeks]}")
        print(":-----------------------------------------------------------------------------------------------:\n")
def total():
    show_data2()
    data = str(input("\nMasukan Nama : "))
    
    print(":--------------------------------------------------------------------------:")
    print("|   Nama   |     Rute Perjalanan     | fasilitas tambahan |  Total Harga   |")
    print(":--------------------------------------------------------------------------:")
    
    for key,value in pembayaran.items():
        if key == data :
           print(f"   {value}      ")
    print(":--------------------------------------------------------------------------:")
# Interaksi Akhir

def interaksi():

    input("\nTekan Enter Untuk Kembali..")

    os.system("cls")

    show_menu()
def show_peserta():
    print(pembayaran.items())

def show_menu():
    print(f"""{Fore.YELLOW}
 ____    _____     __________
|  _  \ |  __  \  |___    ___|
| | )  |  |   \ \     |  |  _ __ __ _     _  ____  _   __ __ _  _ ___
|  __ /   |   | |     |  || '__/  _' |\  / /  _  \| |_/ /  _' || '__/
|  |    | |__/ /      |  || |  | (_| | \/ /   __ /   _ \  (_| || |
|__|    |_____/   o   |__||_|   \__'_|\__/ \_____||_| \_\___'_||_|
{Fore.RESET}""")
    print("\t}"f"{Fore.RED}---------------------------------------------{Fore.RESET}""{")
    print("}"f"{Fore.RED}--------------------- {Fore.GREEN}PD. Travekar{Fore.RESET} {Fore.RED}------------------------{Fore.RESET}""{")
    print("\t}"f"{Fore.RED}---------------------------------------------{Fore.RESET}""{\n")

    print(f"\t{Fore.GREEN}[{Fore.RESET} 1 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Tambah Transaksi Peserta{Fore.RESET}")
    print(f"\t{Fore.GREEN}[{Fore.RESET} 2 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Lihat Daftar Peserta{Fore.RESET}")
    print(f"\t{Fore.GREEN}[{Fore.RESET} 3 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Cari Peserta{Fore.RESET}")
    print(f"\t{Fore.GREEN}[{Fore.RESET} 4 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Exit{Fore.RESET}")

    menu = int(input(f"\n\t{Fore.YELLOW}${Fore.RESET}Pilih Menu >> "))
    if menu ==1:
        tambah_data()
    elif menu == 2:
        show_data()
    elif menu == 3:
        total()
    elif menu == 4:
        show_peserta()
    elif menu == 5:
        exit()
    else:
        print("salah pilih menu")
show_menu()

            
            