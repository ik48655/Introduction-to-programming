"""
Napisati funkciju koja prima rjecnik i jedan broj. Vrijednosti u rjecniku
su liste brojeva. Funkcija vraca True ako se broj nalazi negdje u rjecniku.
"""

def funkyb4(rjecnik,broj):
    for k in rjecnik:
        if broj in rjecnik:
            return True
        return False
    
rjecnik1={3:[1,2,3],4:[4,5,6],5:[7,8,9]}
rjecnik2={"tri":[1,2,"tri"],4:[4,5,6],5:[7,8,9]}
rjecnik3={3:[1,2,4],4:[4,5,6],5:[7,8,9]}
rjecnik4={4:[1,2,3],4:[4,5,6],5:[7,8,9]}

print(funkyb4(rjecnik1,10))
print(funkyb4(rjecnik2,3))
print(funkyb4(rjecnik3,3))
print(funkyb4(rjecnik4,3))