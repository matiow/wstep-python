import platform
import subprocess

imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
try:
    wiek = int( input("Podaj swój wiek: "))
except ValueError as Error:
    wiek = 3
    print(f'wiek ustawiono na {wiek},\nwystąpil: {Error}')
numerKarty = input("Podaj numer karty: ")
kodCVC = input("Podaj numer CVC: ")

def ukryj(nazwaPliku):
    with open(nazwaPliku, mode='w+', encoding='UTF-8') as file:
        file.write(f"""
        {imie}
        {nazwisko}
        {wiek}
        {numerKarty}
        {kodCVC} """)

#sprawdzanie systemu
if platform.system() == 'Windows' :
    ukryj('ukryty.txt')
    print(platform.system())
    subprocess.check_call(["attrib","+H","ukryty.txt"])
elif platform.system() =='Darwin' or platform.system() =='Linux':
    ukryj('.ukryty.txt')