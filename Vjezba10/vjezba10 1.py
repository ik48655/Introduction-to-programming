#Napisati funkciju koja prima listu brojeva i listu stringova.
#Funkcija ispisuje samo stringove na indeksima zadanim u listi brojeva.

def funkc(lista1, lista2):

    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if (i == lista2[j]):
                print(lista1[i])
                
lista1 = ["a", "b", "c", "d","e","f","g","h","i","j"]
lista2 = [0, 2, 3, 4,6,8]

funkc(lista1, lista2)