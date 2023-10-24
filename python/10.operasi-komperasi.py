#setiap hasil dari operasi komparasi adalah bolean 

# >,<,>=,<=,==,!=,is,is not

a = 5
b = 2

#lebih dari 
print('=========================== Lebih dari (>)')
hasil = a > 3 
print(a,'>',3,'=',hasil)
hasil = b > 3 
print(b,'>',3,'=',hasil)

print('=========================== Kurang dari (<)')
hasil = a < 3 
print(a,'<',3,'=',hasil)
hasil = b < 3 
print(b,'<',3,'=',hasil)

print('=========================== Lebih dari sama dengan (>=)')
hasil = a >= 3 
print(a,'>=',3,'=',hasil)
hasil = b >= 3 
print(b,'>=',3,'=',hasil)
hasil = b >= 2 
print(b,'>=',2,'=',hasil)

print('=========================== Kurang dari sama dengan (<=) ')
hasil = a <= 3 
print(a,'<=',3,'=',hasil)
hasil = b <= 3 
print(b,'<=',3,'=',hasil)
hasil = b <= 2 
print(b,'<=',2,'=',hasil)

print(' =============== sama dengan (==)')
hasil = a == 3 
print(a,'==',3,'=',hasil)
hasil = b == 3 
print(b,'==',3,'=',hasil)
hasil = b == 2 
print(b,'==',2,'=',hasil)

print(' =============== sama dengan (!=)')
hasil = a != 3 
print(a,'!=',3,'=',hasil)
hasil = b != 3 
print(b,'!=',3,'=',hasil)
hasil = b != 2 
print(b,'!=',2,'=',hasil)

# is membandingkan  memory /objeck identity
print(' =============== objeck identity (is)')
x =  5 # ini adalah assgnment membuat object 
y = 5 
print('nilai x = ',x,'id =', hex(id(x)))
print('nilai x = ',y,'id =', hex(id(y)))
hasil =  x is y 
print('x is y =', hasil)

print(' =============== objeck identity (is not)')  
x =  5 # ini adalah assgnment membuat object 
y = 6 
print('nilai x = ',x,'id =', hex(id(x)))
print('nilai x = ',y,'id =', hex(id(y)))
hasil =  x is not y 
print('x is not y =', hasil)

#  hex(id(x))) melihat id memory hex


