"""
Napisati funkciju koja cita dva po dva broja dok god korisnik ne upiše oba
pozitivna broja. Funkcija nakon toga vraca ta dva broja.
"""

def pozitivni():
    while True:
        a=int(input("Unesite prvi broj: "))
        b=int(input("Unesite drugi broj: "))
        if a%2==0 and b%2==0:
            return a,b
        else:
            a=int(input("Unesite prvi broj: "))
            b=int(input("Unesite drugi broj: "))
    
print(pozitivni())