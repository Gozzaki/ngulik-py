#latihan membuat list 

list_buku = []
#program list buku
while True:
    print("masukan data buku")
    judul = str(input("masukan Judul = "))
    penulis = str(input("masukan nama penulis = "))

    buku_baru = [judul,penulis,]
    list_buku.append(buku_baru)
    print(list_buku)

    print("No\t|judul\t\t|penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index}\t|{buku[0]}\t\t {buku[1]}")

    print("\n\n","="*20)

    lanjut = input("lanjutkan mengisi data ? (y/n): ")
    if lanjut == "n":
        break


print("as")