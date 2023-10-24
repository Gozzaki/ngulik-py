# #logika dan komparasi 

# #membuat gabungan area rentang dari angka 


# ++++++++3---------10++++++

inputUser = float(input('Masukan angka yang bernilai\nkurang dari 3\natau\nlebih bsear dari 10 :'))

# ++++++3-----------
#memriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print('kurang dari 3',isKurangDari)

#-------------10+++++
#memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print('lebih dari 10',isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan : ", isCorrect)

#-----3+++++++10
#kasus irisan
print("\n",10*"=","\n")
inputUser = float(input('Masukan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10 :'))

#-----3+++++++++++
#lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3",isLebihDari)
#+++++++++++10----
#kurang dari 10
isKurangDari = inputUser < 10
print("kurang dari 10 = ", isKurangDari)

isCorrect = isLebihDari and isKurangDari
print("angka yang anda masukan : ", isCorrect)

#soal latihan -------------------------------------------------------------------------------- soal latihan 
# masukan angka
# ----0+++++5-----8+++++11------

inputUser = float(input("masukan Angka \nlebih dari 0 \ndan kurang dari 5 \ndan lebih dari 8 dan \nkuran dari 11 :"))
#0++++5
isLebihDari0 = inputUser > 0
print("lebih dari 0 = ",isLebihDari0) 

isKurangDari5 = inputUser < 5
print("Kurang dari 5 = ",isKurangDari5) 

hasil1 = isKurangDari5 and isLebihDari0
print("0++++5 =" ,hasil1)
#8++++++11

isLebihDari8 = inputUser > 8
print("lebih dari 0 = ",isLebihDari8) 

isKurangDari11 = inputUser < 11
print("Kurang dari 5 = ",isKurangDari11) 

hasil2 = isKurangDari11 and isLebihDari8
print("8++++11 =" ,hasil2)
isCorrect = hasil1 ^ hasil2
print("angka yang anda masukan : ", isCorrect)
#-------------------------------------------------------------------------- /soal 1


#+++++0-----5+++++8-----11++++++

#++++0
#memriksa angka kurang dari 0
inputUser = float(input("+++++0-----5+++++8-----11++++++\nmasukan angksa range di atas : "))
isKurangDari = (inputUser < 3)
print('kurang dari 0',isKurangDari)

#-------------11+++++
#memeriksa angka lebih dari 11
isLebihDari = (inputUser > 11)
print('lebih dari 10',isLebihDari)

hasil1 = isKurangDari or isLebihDari
print("+++0-----11++++ : ", hasil1)


#5+++++8

isLebihDari5 = inputUser > 5
print("lebih dari 5 = ",isLebihDari5) 

isKurangDari8 = inputUser < 8
print("Kurang dari 8 = ",isKurangDari8) 

hasil2 = isLebihDari5 and isKurangDari8
print("5++++8 =" ,hasil2)

isCorrect = hasil1 or hasil2
print("angka yang anda masukan : ", isCorrect)
#------------------------------------------------------------------------/soal2


#------------- cari lain soal 1 ---------------
# ----0+++++5-----8+++++11------
InputUser = float(input("masukan Angka \nlebih dari 0 \ndan kurang dari 5 \ndan lebih dari 8 dan \nkuran dari 11 :"))
# Cara 2 soal 1
IsLebihDari0KurangDari5 = InputUser > 0 and InputUser < 5
IsLebihDari8KurangDari11  = InputUser > 8 and InputUser < 11
Cara2Soal1 = IsLebihDari0KurangDari5 or IsLebihDari8KurangDari11
print("Status Cara 2: ", Cara2Soal1)

# Cara 3
Cara3Soal1 = 0 < InputUser < 5 or 8 < InputUser < 11
print("Status Cara 3: ", Cara3Soal1)
#------------------------------------------------/

#------------- cari lain soal 2 ---------------
#+++++0-----5+++++8-----11++++++
InputUser = float(input("+++++0-----5+++++8-----11++++++\nmasukan angksa range di atas : "))
# Cara 2 soal 2
IsKurangDari0 = InputUser < 0
IsLebihDari5KurangDari8  = InputUser > 5 and InputUser < 8
IsLebihdari11  = InputUser > 11
Cara2Soal2 = IsKurangDari0 or IsLebihDari5KurangDari8 or IsLebihdari11
print("Status Cara 2: ", Cara2Soal2)

# Cara 3 soal 2
Cara3Soal2 = InputUser < 0 or 5 < InputUser < 8 or InputUser > 11 
print("Status Cara 3: ", Cara3Soal2)
#--------------------------------------------------/