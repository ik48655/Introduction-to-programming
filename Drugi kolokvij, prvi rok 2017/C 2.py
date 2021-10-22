"""
Napisati program koji od korisnika cita slova. Ako korisnik ne upiše slovo
program ponavlja unos. Ako korisnik upiše tocku, program završava i
ispisuje broj upisanih suglasnika i samoglasnika.
"""
lstslov=[]
samogl=0
sugl=0
while True:
    char1=str(input("Unesite neko slovo: "))
    if len(char1)==1:
        lstslov.append(char1)
        if char1==".":
            break
        if char1 in "AEIOUaeiou":
            samogl=samogl+1
        else:
            sugl=sugl+1
    else:
        print("Niste unijeli slovo, greška.")
print("Broj samoglasnika je: ",samogl,"Broj suglasnika je: ",sugl)