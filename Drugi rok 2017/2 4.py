"""
Napisati funkciju koja prima rjecnik i broj B. Vrijednosti u rjecniku su
liste brojeva. Funkcija vraca True ako su svi brojevi u svim listama u
rjecniku manji od B.
"""

def funky4(rjecnik,B):
    for k in rjecnik:
        for e in rjecnik[k]:
            if e >= B:
                return False
    return True
    
    
rjecnik1={"prvi":[1,2,3,4],"drugi":[5,6,7,8],"treci":[9,2,11,12]}
print(funky4(rjecnik1,13))
    

    