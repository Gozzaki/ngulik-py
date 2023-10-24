# operasi logika atau boolean 
# not  or , and , xor

# NOT
print('====NOT====')
a = True
b = False
c = not a
print('data a= ', a)
print('-------------- NOT')
print('data c not a = ', c)

# OR Jika salah satu True , maka hasil nya (True)
print('====OR====')
a = False 
b = False
c = a or b
print(a,'OR',b, '=', c)
a = False 
b = True
c = a or b
print(a,'OR',b,' =', c)
a = True 
b = False
c = a or b
print(a,' OR',b,'=', c)
a = True 
b = True
c = a or b
print(a,' OR',b, ' =',c)

# AND (jika dua buah nilai Treue , maka hasio nya  True )
print('====AND====')
a = False 
b = False
c = a and b
print(a,'AND',b, '=', c)
a = False 
b = True
c = a and b
print(a,'AND',b,' =', c)
a = True 
b = False
c = a and b
print(a,'AND',b,'=', c)
a = True 
b = True
c = a and b
print(a,'  AND',b, ' =',c)

#XOR (akan Ture jika salh satu True , sisa nya False)
print('====XOR====')
a = False 
b = False
c = a ^ b
print(a,'XOR',b, '=', c)
a = False 
b = True
c = a ^ b
print(a,'XOR',b,' =', c)
a = True 
b = False
c = a ^ b
print(a,'XOR',b,'=', c)
a = True 
b = True
c = a ^ b
print(a,'  XOR',b, ' =',c)