"""
Napisati funkciju koja prima rjecnik koji kao kljuceve ima brojeve, a kao
vrijednosti liste brojeva. Funkcija vraca True ako je svaki kljuc jednak
zbroju pridružene liste.
"""

def zbr_vri_je_k(dictionary):
    brojac=0
    for k,v in dictionary.items():
        suma=0
        for broj in v:
            suma+=broj
        if k == suma:
            brojac+=1
    if brojac == len(dictionary):
        return True
    return False
   
rjecnik1={24:[7,8,9],
          15:[4,5,6],
          6:[1,2,3]}

print(rjecnik1)
print(zbr_vri_je_k(rjecnik1))
    