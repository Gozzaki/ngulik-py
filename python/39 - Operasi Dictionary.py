# operator dictionary 

data_dict = {
    "lie" : "gozalie",
    "wali" : "ahmad awali",
    "neng" : "tasya rahmah"
}

# cek panjang dictionary menggunakan  len()
lendict = len(data_dict)
print(f"panjang dari dictionnary = {lendict}")


# mengecek key axist atau tidak
KEY = "lie"   #variabel konstanta menggunakan huruf kapital semua
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict : {CHECKKEY}")

# menggakses value (read) dengan get 
print(data_dict["lie"])
print(data_dict.get("lie"))
print(data_dict.get("wow","key tidak ditemukan")) #cek key dengan tambahan pesan jika tidak ditemukan

#mengupdate data 
print(15*"=","update data\n")
data_dict["lie"] = "gozali ali atamimi"
print(data_dict)
print(15*"=","menambah data\n")
data_dict["otong"] = "otong surotong"
print(data_dict)
print(15*"=","update datamenggunakan update({}) \n")
data_dict.update({"lie" : "gozali si kasep"})
print(data_dict)
print(15*"=","update datamenggunakan update({}) \n") #jika key tidak di temukan maka akan menambah data dengan key baru
data_dict.update({"bayu" : "pak bayu uuuu"})
print(data_dict)

# mendelete data pada dictionary
print(15*"=","delete\n")
del data_dict["bayu"]
print(data_dict)
