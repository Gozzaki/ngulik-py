# format string


#contoh generic

nama = "gozali" #cara lama
str = "hello "+ nama
print(str)
print("--- string")
format_str = f"heloo {nama}" #menggunkakn format
print(format_str)

#bolean 
print("--- boolean")

boolean = True
format_str = f"boolean = {boolean}"
print(format_str)
# anhka 

print("--- angka")
angka = 2003.6
# format_str = "angka = " + str(angka)  #cara lama 
#print(format_str)

format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat 

angka = 15
format_str = f"bilangan bulat = {angka:d}" # d untuk membuat bilangan str
print(format_str) # kaga penting

#bilangan ribuan 
angka = 2000
format_str = f"ribuan = {angka:,}" # koma untuk membuat angka menjadi rupiah / ribuan 
print(format_str)

#bilangan desimal
angka = 2003.54321
format_str = f"angka = {angka:.3f}" #.3f untuk mengambil 3 angka dari titik
print(format_str)

# menampilkan leading zero
angka = 2003.54321
format_str = f" leading zero angka = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# memformat persen 
presentase = 0.045
format_persen = f"persen = {presentase:.2%}"
print(format_persen)

# melakukan operaasi aritmatika di dalam placeholder
harga = 100000
jumlah = 5
format_string = f"harga total = {harga*jumlah:,}"
print(format_string)

# format angka lain (binary , octal , hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)

tahun = 2023
bulan = 10
hari = 5
tanggal = f"{tahun}-{bulan:02d}-{hari:02d}"
print(tanggal)



