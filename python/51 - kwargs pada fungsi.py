'''**kwargs'''

def fungsi (nama,tinggi,berat):
    '''fungsi Biasa'''
    print(f"{nama} Punya tunggi {tinggi} dan Berat {berat}")

fungsi("ucup",188,79)

def fungsi(**kwargs):
    '''Funsi Kwargs'''
    print(kwargs)

fungsi(nama="ucup",tinggi =189,berat=78)

def fungsi(**kwargs):
    '''Funsi Kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} Punya tunggi {tinggi} dan Berat {berat}")

fungsi(nama="ucup",tinggi =189,berat=78)

#studi kasus

def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output +=angka
        print("operasi penjumlahan")
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *=angka
        print("operasi perkalian")
    return output

hasil = math(1,2,3,option="tambah")
print(f"Hasil Jumlah = {hasil}")
hasil = math(1,2,3,4,option="kali")
print(f"Hasil kali = {hasil}")
