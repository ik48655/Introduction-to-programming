#Napisati funkciju koja prima rječnik gdje su ključevi imena kandidata, a vrijednost broj glasova koje je
#dobio na izborima. Funkcija vraća novi rječnik koji sadrži imena kandidata i postotak dobivenih
#glasova

def funkcija(rijecnik):
    rijecnik = {}
    broj_glasova = 0
    for e in rijecnik:
        broj_glasova += rijecnik[e]
    for e in rijecnik:
        postotak = (rijecnik[e]/broj_glasova)*100
        rijecnik[e] = str(int(postotak))+"%"
    return rijecnik

rijecnik = {"ivan" : 23, "petar" : 18, "iva" : 55, "aleksandra" : 11 }
print(funkcija(rijecnik))