# Latihan konversi Satuan Temperatur

# Program Konversi Celcius Ke Satuan Lain Nya

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("masukan Suhu Dalam Celcius :"))

print("Suhu Adalah", celcius , "Celcius")

#Reamur 
reamur = (4/5) * celcius
print("Suhu Dalam Reamur Adalah", reamur , "Reamur")

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu Dalam Fahrenheit Adalah", fahrenheit , "Farenheit")

#Kelvin 
kelvin = celcius + 273
print("Suhu Dalam Kelvin Adalah", kelvin , "Kelvin")

