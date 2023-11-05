#copy dictionary

teman_teman = {
    "ong" : "ong wang surudug soang",
    "tong" : "otong pararotong",
    "ler" : "epe ep ler",
    "aeps" : "aeps si kasep",
    "bay" :   "pak bay bay"
}

kawan_kawan = teman_teman.copy()
print(f"teman_teman : {teman_teman}\n")
print(f"kawan_kawan : {kawan_kawan}\n")

teman_teman["ler"] = "ler si beler"
print(f"teman_teman : {teman_teman}\n")
print(f"kawan_kawan : {kawan_kawan}\n")

# pop() dictionary mengtransfer (berdasarkan key)
dataBay = kawan_kawan.pop("bay")
print(f"data Bay = {dataBay}")
print(f"kawan_kawan : {kawan_kawan}\n")

# popitem() dictionary mengtransfer ( data yang terakhir)
dataTrakhir = kawan_kawan.popitem()
print(f"data Terakhir = {dataTrakhir}")
print(f"kawan_kawan : {kawan_kawan}\n")

