print(f"{5*'='} Kalkulator sederhana {5*'='}")

angka_1 = float(input("Masukan Angka 1 :\t"))
operator = str(input("Masukan Operator +/-/*/% :\t"))
angka_2 = float(input("Masukan Angka 2 :\t"))

if operator == "+":
    hasil = angka_1 + angka_2 
    print(f"{angka_1} + {angka_2} = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2 
    print(f"{angka_1} + {angka_2} = {hasil}")
elif operator == "*" or "x":
    hasil = angka_1 * angka_2 
    print(f"{angka_1} * {angka_2} = {hasil}")
elif operator == "%":
    hasil = angka_1 % angka_2 
    print(f"{angka_1} % {angka_2} = {hasil}")
else:
    print(f"{operator} Tidak terbaca sebagai Operator")