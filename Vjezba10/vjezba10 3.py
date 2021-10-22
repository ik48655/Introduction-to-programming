#Napisati funkciju koja prima dvije liste riječi. Funkcija vraća listu riječi koje se pojavljuju u obje liste.

def funkc(lista1, lista2):
    
    listaF = []
    
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if (lista1[i] == lista2[j]):
                listaF.append(lista1[i])
    return listaF

lista1 = ["jedan", "dva", "tri", "èetri" , "pet", "šest"]
lista2 = ["jedan", "tri", "šest", "osan", "devet", "deset"]

listaF = funkc(lista1, lista2)

print(listaF)