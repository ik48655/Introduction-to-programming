"""
Napisati funkciju koja cita tri po tri broja dok god korisnik ne unese jedan
parni broj, jedan neparni broj i nulu u bilo kojem redoslijedu. Funkcija
nakon toga vraca ta tri broja.
"""

def tripotri(a,b,c):
        a=int(input("Unesite prvi broj: "))
        b=int(input("Unesite drugi broj: "))
        c=int(input("Unesite treci broj: "))
        while True:
            if a%2==0 and ((b%2!=0 and c==0) or (b==0 and c%2!=0)):
                return a,b,c
            elif b%2==0 and ((a%2!=0 and c==0) or (a==0 and c%2!=0)):
                return a,b,c
            elif c%2==0 and ((b%2!=0 and a==0) or (b==0 and a%2!=0)):
                return a,b,c
            else:
                a=int(input("Unesite prvi broj: "))
                b=int(input("Unesite drugi broj: "))
                c=int(input("Unesite treci broj: "))
            
print(tripotri(0,0,0))
            