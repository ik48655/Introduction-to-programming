"""
Napisati funkciju koja prima rjecnik gdje su kljucevi i vrijednosti stringovi.
Funkcija vraca novi rjecnik gdje su kljucevi i vrijednosti dobivenog rjecnika
zamijenjeni.
"""
def funky6(rj):
    rj2 = dict()
    for key, value in rj.items():
        rj2.setdefault(value, key)
    return rj2

rj1={"abc":"def","ghi":"jkl","mno":"pqr","stu":"vwx"}
print(rj1)
print(funky6(rj1))
            