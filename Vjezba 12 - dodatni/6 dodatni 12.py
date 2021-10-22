"""
6.	Napisati funkciju koja prima rječnik gdje su ključevi i vrijednosti stringovi.
 Funkcija vraća novi rječnik gdje su ključevi i vrijednosti dobivenog rječnika
 zamijenjeni.
"""

def funky6(rj):
    rj2 = dict()
    for key, value in rj.items():
       rj2[value]=key
    return rj2

rj1={"abc":"def","ghi":"jkl","mno":"pqr","stu":"vwx"}
print(rj1)
print(funky6(rj1))