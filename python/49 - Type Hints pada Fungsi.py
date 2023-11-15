'''Type Hint Untuk Fungsi'''

# bentuk standar fungsi yang udah di pelajari

'''
Studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("UCUP")
fungsi(True)
'''

#penggunaan type hints
import string
def sepuluh_pangkat(argument:int)-> int:
    '''Fungsi Dengan Hints'''
    output = 10** argument
    return output

hasil = sepuluh_pangkat(2)

print(f"{hasil}")

def display(argument:string):
    print(argument)

display("ucup")
