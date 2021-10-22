"""
Napisati funkciju koja prima rjecnik sa stringovima kao kljucevima i listama
brojeva kao vrijednostima. Za svaki kljuc u rjecniku, funkcija racuna
zbroj pridružene liste. Funkcija vraca rjecnik sastavljen od istih kljuceva
i pridruženih zbrojeva lista.
"""

def zbroj_vrijednosti(dictionary):
    for k in dictionary:
        zbroj=0
        for v in dictionary[k]:
            zbroj+=v
            dictionary[k]=zbroj
    return dictionary
   
rjecnik1={"jedan":[7,8,9],
          "dva":[4,5,6],
          "tri":[1,2,3]}

print(rjecnik1)
print(zbroj_vrijednosti(rjecnik1))
