"""
3.	Napisati funkciju koja prima rječnik i jedan broj. Vrijednosti u rječniku 
su liste brojeva. Funkcija vraća True ako se broj nalazi negdje u rječniku.
"""

def funk3(rj,B):
    for k in rj:
        for v in rj[k]:
            if B in rj[k] or B in rj:
                return True
    return False

rj1={"prvi":[1,2,3],
     "drugi":[4,5,6],
     "treci":[7,8,9],
     "cetvrti":[10,11,12]
     }
rj2={"sedam":[1,2,3],
     "drugi":[4,5,6],
     "treci":[6,8,9],
     "cetvrti":[10,11,12]
     }
rj3={6:[1,2,3],
     "drugi":[4,5,6],
     "treci":[7,8,9],
     "cetvrti":[10,11,12]
     }


print(funk3(rj1,3))
print(funk3(rj2,7))
print(funk3(rj3,6))


    