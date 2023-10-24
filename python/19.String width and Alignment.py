
# width and multiline

data_nama = "gozali"
data_umur = 20
data_tinggi = 168.0

# string 

data_string = f"nama = {data_nama}, umur = {data_umur}, Tinggi = {data_tinggi}"
print(f"{5*'='} Data String {5*'='}")
print(data_string)

# String multiline (dengan menggunkan enter , nerwline , \n)
data_string = f"nama = {data_nama},\numur = {data_umur},\nTinggi = {data_tinggi}"
print(f"{5*'='} Data String {5*'='}")
print(data_string)

# String multiline  (kutip triplets)

data_string = f"""nama = {data_nama},
umur = {data_umur},
separu = {data_tinggi}
"""
print(f"{5*'='} Data String {5*'='}")
print(data_string)

# mengatur lebar  (:>7 akan rata kanan)
data_string = f"""
nama   = {data_nama:>7}, 
umur   = {data_umur:>7},
separu = {data_tinggi:>7}
"""
print(f"{5*'='} Data String {5*'='}")
print(data_string)







