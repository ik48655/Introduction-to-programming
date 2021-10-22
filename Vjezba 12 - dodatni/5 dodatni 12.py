"""
5.	Napisati funkciju koja prima rječnik sa stringovima kao ključevima i listama
 brojeva kao vrijednostima. Za svaki ključ u rječniku, funkcija računa najveći 
 broj iz pridružene liste. Funkcija vrača rječnik sastavljen od istih ključeva 
 i pridruženih najvećih brojeva.
"""

def funk5(rjecnik):
    for k in rjecnik:
        najv=rjecnik[k][0]
        for e in rjecnik[k]:
            if e > najv:
                najv=e
        rjecnik[k]=najv
    return rjecnik
                
                
                
                
rjecnik1 = {"ab":[1,2,3],"cd":[4,5,6],"ef":[7,8,9]}

print(funk5(rjecnik1))                