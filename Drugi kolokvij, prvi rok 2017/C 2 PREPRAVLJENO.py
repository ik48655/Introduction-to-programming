"""
Napisati program koji od korisnika cita slova. Ako korisnik ne upiÅ¡e slovo
program ponavlja unos. Ako korisnik upiÅ¡e tocku, program zavrÅ¡ava i
ispisuje broj upisanih suglasnika i samoglasnika.
"""
lstslov=[]
samogl=0
sugl=0
while True:
    char1=str(input("Unesite neko slovo: "))
    if char1==".":
        break
    if len(char1)==1 and char1.isalpha():
        lstslov.append(char1)
        if char1 in "AEIOUaeiou":
            samogl=samogl+1
        else:
            sugl=sugl+1
    else:
        print("Niste unijeli slovo, greska.")
print("Broj samoglasnika je: ",samogl,"Broj suglasnika je: ",sugl)