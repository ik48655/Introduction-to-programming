"""
Napisati funkciju koja prima rjecnik koji kao kljuceve ima brojeve, a kao
vrijednosti liste brojeva. Funkcija vraca True ako je svaki kljuc jednak
zbroju pridružene liste.
"""

def funky4(rjecnik):
    for k in rjecnik:
        zbroj=0
        for v in rjecnik[k]:
            zbroj=zbroj+v
        if zbroj != k:
            return False
    return True


rjecnik1={6:[1,2,3],15:[4,5,6],24:[7,8,9]}
rjecnik2={6:[1,2,3],15:[4,5,6],23:[7,8,9]}
rjecnik3={6:[1,2,3],14:[4,5,6],22:[7,8,9]}
rjecnik4={5:[1,2,3],13:[4,5,6],21:[7,8,9]}

print(funky4(rjecnik1))
print(funky4(rjecnik2))
print(funky4(rjecnik3))
print(funky4(rjecnik4))

            