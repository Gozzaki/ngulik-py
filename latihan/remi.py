from colorama import Fore
import os
list_pemain = []
def seting_pemain ():
    while True:
        menu = int(input(f"\n\t{Fore.YELLOW}${Fore.RESET}Masukan Jumlah Pemain (3->5) >> "))
        if menu <3 or menu >5 :
            print(f"\t {Fore.RED}Salah Memasukan Jumlah Pemain{Fore.RESET}")
            continue
        break
        
    tambah_pemain= []

    list_pemain.append(tambah_pemain)

    for i in range(menu):
        tambah_pemian = str(input(f"\n\t{Fore.YELLOW}${Fore.RESET}Pemain {i+1} >> "))
        list_pemain.append(tambah_pemian)
    
    print(f"\t{Fore.GREEN}Setting Pemain berhasil{Fore.RESET}")
    exit = str(input(f"\tUntuk Kembali Ke Menu Utama Tekan (Y)")).upper()
    if exit == "Y":
        show_menu()

def mulai_main ():
    print("mainkan")

def seting_peraturan():
    menu = int(input(f"\n\t{Fore.YELLOW}${Fore.RESET}Masukan Jumlah Peraturan >> "))

def total():
    for i in range(len(list_pemain)):
        print(f"Pemain {i+1}\t|\t{list_pemain[i]}\n")
    print(f"\t{Fore.GREEN}Setting Pemain berhasil{Fore.RESET}")
    exit = str(input(f"\tUntuk Kembali Ke Menu Utama Tekan (Y)")).upper()
    if exit == "Y":
        show_menu()

def show_menu():
    print(f"""
                                                            
                                                            
               :^~^.                         {Fore.RED}..{Fore.RESET}               
             7G####GJ.                      {Fore.RED}^JJ~{Fore.RESET}              
            !&######&J                    {Fore.RED}:?YYYY?^{Fore.RESET}            
          :^Y########P~:                {Fore.RED}.7YYYYYYYY7:{Fore.RESET}          
        ^5B#############P~            {Fore.RED}.!JYYYYYYYYYYY!.{Fore.RESET}        
       .B&################:           {Fore.RED}~YYYYYYYYYYYYYY~{Fore.RESET}        
        5&##############&G.            {Fore.RED}:7YYYYYYYYYY7:{Fore.RESET}         
        .7PGBBP7YP7PGBBP?.               {Fore.RED}:?YYYYYY?^{Fore.RESET}           
           ... ^B#~ ...                    {Fore.RED}^JYYJ~ {Fore.RESET}            
             :J5PPPY^                       {Fore.RED}.~!.{Fore.RESET}              
                                                            
                                                            
                                                            
                                                            
{Fore.RED}         ^!77!~:  :~!77!^.{Fore.RESET}                 :?^              
{Fore.RED}       :?YYYYYYY?7YYYYYYYJ^{Fore.RESET}              .?B&#Y:            
{Fore.RED}       JYYYYYYYYYYYYYYYYYYY.{Fore.RESET}            7B&#####J:          
{Fore.RED}       !YYYYYYYYYYYYYYYYYY?{Fore.RESET}           ~P########&B?.        
{Fore.RED}        ~JYYYYYYYYYYYYYYY!.{Fore.RESET}         .Y############&G^       
{Fore.RED}         .7YYYYYYYYYYYY?:{Fore.RESET}           J&#############&G       
{Fore.RED}           :?YYYYYYYYJ^{Fore.RESET}             ~B&###&###&###&#?       
{Fore.RED}             ^?YYYYJ~{Fore.RESET}                .7Y5Y?!B?7Y5Y?^        
{Fore.RED}               ^JJ!.{Fore.RESET}                     .!5&G7:            
{Fore.RED}                ..{Fore.RESET}                       .~~~~~^            
                                                            
                                                           
""")
    print("\t}"f"{Fore.RED}---------------------------------------------{Fore.RESET}""{")
    print("}"f"{Fore.RED}--------------------- {Fore.GREEN}REMI BOX{Fore.RESET} {Fore.RED}------------------------{Fore.RESET}""{")
    print("\t}"f"{Fore.RED}---------------------------------------------{Fore.RESET}""{\n")

    print(f"\t{Fore.GREEN}[{Fore.RESET} 1 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Tambah Transaksi Peserta{Fore.RESET}")
    print(f"\t{Fore.GREEN}[{Fore.RESET} 2 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Lihat Daftar Peserta{Fore.RESET}")
    print(f"\t{Fore.GREEN}[{Fore.RESET} 3 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Cari Peserta{Fore.RESET}")
    print(f"\t{Fore.GREEN}[{Fore.RESET} 4 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Exit{Fore.RESET}")

    menu = int(input(f"\n\t{Fore.YELLOW}${Fore.RESET}Pilih Menu >> "))
    if menu == 1:
        seting_pemain()
    elif menu == 2:
        mulai_main()
    elif menu == 3:
        seting_peraturan()
    elif menu == 4:
        total()
    elif menu == 5:
        exit()
    else:
        print("salah pilih menu")
show_menu()