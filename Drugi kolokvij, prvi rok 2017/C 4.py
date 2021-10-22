"""
Napisati funkciju koja prima rjecnik sa stringovima kao kljucevima i listama
brojeva kao vrijednostima. Za svaki kljuc u rjecniku, funkcija racuna
najveci broj iz pridružene liste. Funkcija vraca rjecnik sastavljen od istih
kljuceva i pridruženih najvecih brojeva.
"""
rjecnik = {"ab":[1,2,3],"cd":[4,5,6],"ef":[7,8,9]}

def najvvrijed(rj):
    for k in rj:
        najv=rj[k][0]
        for e in rj[k]:
            if e > najv:
                najv = e
        rj[k] = najv
    return rj

print(najvvrijed(rjecnik))