#Napisati program koji od korisnika čita stringove i sprema ih u listu. Kada korisnik upiše samo točku,
#program završava i ispisuje sve stringove iz liste koji su duži od 5 znakova.

lista = []
while True:
    string = input("Unesite string: ")
    if string == ".":
        for e in lista:
            if len(e)>5:
                print(e)
        break
    else:
        lista.append(string)
        print(lista)