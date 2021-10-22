"""
Napisati funkciju koja prima rjecnik i jedan broj. Vrijednosti u rjecniku
su liste brojeva. Funkcija vraca True ako se broj nalazi negdje u rjecniku.
"""

def ifNuListi(dictionary,n):
    for k in dictionary:
        if n in dictionary[k]:
            return True
    return False
            
            
rjecnik1={"jedan":[7,8,9],
          "dva":[4,5,6],
          "tri":[1,2,3]}


print(ifNuListi(rjecnik1,11))
    
                