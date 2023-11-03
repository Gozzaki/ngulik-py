# Looping Doctionary

teman_teman = {
    "ong" : "ong wang surudug soang",
    "tong" : "otong pararotong",
    "dung" : "dudung surudung",
    "aeps" : "aeps si kasep",
    "bay" :   "pak bay bay"
}

# looping first try (yang keluar adalah key nya)
print(f"\n{10*'='} coba loop menggunakan metode list\n")
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item / iterebel
print(f"\n{10*'='} hanya mengambil key\n")
keys = teman_teman.keys() #untuk mengambil keys nya saja dalam dictionary
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

print(f"\n{10*'='} hanya mengambil value\n")
values = teman_teman.values() # untuk mengambil value nya saja
print(values) 

for value in teman_teman.values():
    print(values)