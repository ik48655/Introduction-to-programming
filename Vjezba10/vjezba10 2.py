#Napisati funkciju koja prima listu parova i vraća dvije liste. 
#Prva lista sadrži samo prve elemente parova, a druga lista druge elemente parova.

def funkc(lista):
    
    lista1 = []
    lista2 = []
    
    for (a, b) in lista:
        lista1.append(a)
        lista2.append(b)
        
    return lista1, lista2


lista = [(2, 3), (3, 4), (4, 5), (5, 6)]

lista1, lista2 = funkc(lista)

print(lista1, lista2)