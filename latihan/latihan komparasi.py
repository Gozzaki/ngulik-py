# latihan komparasi dan logika

#------0++++++5------8++++++11------
print ("SOAL 1 ---0+++5---8+++11---")
inputUser = float(input("masukan angka bernilai\nlebih dari 0\ndan \nkurang dari 5\natau\nlebih dari 8\ndan\njurang dari 11 :"))
#mencari lebih dari 0 dan kurang dari 5
lebihdari0 = inputUser > 0
kurangdari5 = inputUser < 5
hasil1 = kurangdari5 and lebihdari0

#mencari lebih dari 8 dan kurang dari 11
lebih8 = inputUser > 8
kurang11 = inputUser < 11
hasil2 = lebih8 and kurang11

akhir = hasil1 ^ hasil2

print ("angka yg anda masukan",akhir)

inputUser = float(input("masukan angka bernilai\nkurang dari 0\natau\nlebih dari 5\ndan \nkurang dari 8\ndan\nlebih dari 11 :"))

data1 = inputUser < 0
data2 = inputUser > 5
data3 = inputUser < 8
data4 = inputUser >11

akhir = (data1 ^ data2) and (data3 ^ data4)

print ("angka yg anda masukan", akhir)
