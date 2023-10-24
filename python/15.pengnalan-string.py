data = "ini string"
print(data)
print(type(data))

# 1. cara membuat string 

''' 
    1. mengunakan singgel quote '....'
    2. mengunakan dobble quote "...."
    3

'''

data = 'menggunakan singel quote'
print(data)

data = "menggunakan singel quote"
print(data)

print('"haloo , apa kabar"')
print("'haloo , apa kabar'")
print("ini adalah hari jum'at")

# 2. Mengunakan tanda \

# membuat tanda ' menjadi sting
print('mari kita sholat jum\'at')
print('g\'day, isn\' it?')

#backlash
print("C:\\user\\Gojay")

# tab 
print("ucup \t\t\t\totong, menjadi jauhan")
print("ucup \botong")

#new line 
print("baris pertama.\nbaris ke dua") #LF ->line feed
print("baris pertama.\rbaris kedua.") # CR -> carriage return
print("baris pertama.\r\nbaris kedua.") #CRLF -> line feed carriage return ->dipakai oleh windows

# 3. stirng literal ataw raw

#hati hati 
print('C:\new folder') # akan salah pathnya

# mengunaka row string
print(r'C:\new folder')

#multiline literal string
print("""
Nama : Gojay 
Kelas : IF21B
""")

# Multiline literal string dan raw
print(r"""
Nama : Gojayyy 
Kelas : IF21B
Website : www.gojay.com/newID
""")

