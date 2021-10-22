#Napisati funkciju koja prima dvije liste riječi. Funkcija vraća rječnik koji sadrži riječi iz prve liste kao
#ključeve i boolean vrijednosti koja označava da li se riječ pojavljuje u drugoj listi.

def dv_liste(lista1, lista2):
    rijecnik = {}
    for e in lista1:
        if e in lista2:
            rijecnik[e] = True
        else:
            rijecnik[e] = False
    return rijecnik

listajed = ["pismo", "glava", "knjiga", "laptop", "nebo", "sunce", "auto"]
listadv = ["ptica", "stol", "pismo", "knjiga", "auto", "mjesec",]

print(dv_liste(listajed,listadv))