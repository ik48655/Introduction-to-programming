#Napisati funkciju koja prima listu brojeva i vraća listu booleana. Svaki element u listi booleana (osim
#prvog) će odgovarati jednom elementu u listi brojeva. Element će biti True ako je broj na istom
#indeksu veći od broja na prethodnom indeksu.

def vracaboolean(lista):
    lista=[True]
    for i in range(len(lista)-1):
        if lista[i+1]>lista[i]:
            lista.append(True)
        else:
            lista.append(False)
    return lista

lista=[2,4,12,6,3,5,11,22]
nova = vracaboolean(lista)
print(nova)