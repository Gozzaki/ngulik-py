''' Fungsi Dengan argument (input)'''

# def nama_fungsi(argument/parameter/input):
    #badan fungsi

def hello_world(nama):
    '''fungsi hello word menerima dengan variabel nama '''
    print(f"selamat datang dunia wahai {nama}")


hello_world("ucuep")
hello_world("jayjay")


# program tambah 

def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(f"hasil {angka_1} + {angka_2} = {hasil}")

tambah(1,8) 
tambah(10000,2) 

def para_suhu(sepuh):
    list_sepuh = sepuh.copy()

    for i in list_sepuh:
        print(f"hai sepuh {i}")

nama = ['yoga otong' , 'rico andrean' ,'bayman','lie']
para_suhu(nama)