"""
Napisati funkciju koja prima listu brojeva. Funkcija vraca listu koja sadrži
boolean vrijednosti. Vrijednost u listi je True samo ako je taj broj djeljiv
sa iducim brojem. Npr. za listu [6,3,1,4,2,4], funkcija vraca [T,T,F,T,F,F].
"""

def djeljiv_s_sljedecim(lst):
    boolbrojevi=[]
    for i in range(len(lst)-1):
        if lst[i] % lst[i+1] == 0:
            boolbrojevi.append(True)
        else:
            boolbrojevi.append(False)
    boolbrojevi.append(False)
    return boolbrojevi
    
        
brojevi=[6,3,1,4,2,4]

print(djeljiv_s_sljedecim(brojevi))
    

