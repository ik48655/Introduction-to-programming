"""
Napisati funkciju koja prima rjecnik sa stringovima kao kljucevima i listama
brojeva kao vrijednostima. Za svaki kljuc u rjecniku, funkcija racuna
najveci broj iz pridružene liste. Funkcija vraca rjecnik sastavljen od istih
kljuceva i pridruženih najvecih brojeva.
"""

def funkyd4(rjecnik):
    for k in rjecnik:
        najv=rjecnik[k][0]
        for e in rjecnik[k]:
            if e>najv:
                najv=e
        rjecnik[k]=najv
    return rjecnik
            
                


rjecnik1={"prvi":[1,2,3],"drugi":[4,5,6],"treci":[7,8,9]}

print(funkyd4(rjecnik1))
            
