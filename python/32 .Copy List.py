#teknik menduplikkat list

a = ["gozali", "gozzaki", "zakia"]
print(f"a = {a}")

b = a  # address akan sama 
print(f"b = {b}")

# kira akan merubah member a

#ini akan merubah kedua list 
a[1] = "lielie"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list
print(f"addrees  a = {hex(id(a))}")
print(f"addrees  b = {hex(id(b))}")


#menduplikat list menggunakan copy
print(f"memvuat list c dengat a.copy()")
c = a.copy() #data baru dengan addres akan berbeda
print(f"addrees  a = {hex(id(a))}")
print(f"addrees  b = {hex(id(b))}")
print(f"addrees  c = {hex(id(c))}")

print(f" kita ubah data 0")
c[1] = "gozzaki" # cara merubah data pada list index ke 1
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")









