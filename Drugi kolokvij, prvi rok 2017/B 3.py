"""
Napisati program koji od korisnika cita stringove i sprema ih u listu. Kada
korisnik upiše samo tocku, program završava i ispisuje sve stringove iz listi
koji su duži od 5 znakova.
"""
lststr=[]
while True:
    string1=str(input("Unesite neki string: "))
    lststr.append(string1)
    if string1==".":
        break
for e in lststr:
    if len(e)>5:
        print(e)
                    
        