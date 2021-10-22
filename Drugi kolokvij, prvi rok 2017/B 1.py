"""
Napisati funkciju koja prima listu lista. Funkcija vraca listu koja sadrži
duljine svih primljenih lista. Npr. za [ [1,2], [], [2] ], funkcija vraca [2,0,1].
"""

def funkyb1(lst):
    lst2=[]
    for i in lst:
        duljina=len(i)
        lst2.append(duljina)
    return lst2


lst3=[[1,2],[],[2]]
print(funkyb1(lst3))
        