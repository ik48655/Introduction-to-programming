"""
Napisati funkciju koja prima listu brojeva. Funkcija vraca listu brojeva iz
primljene liste koji su nisu djeljivi sa nijednim drugim brojem iz primljene
liste. Npr. za listu [ 6, 2, 7, 9 ], funkcija vraca listu [2,7,9].
"""
def nedjeljivi(lst):
    nedjeljivibr=[]
    duzina=0
    while duzina < len(lst):
        flag = True
        prvi=duzina
        for i in range(len(lst)-1):
            if prvi % lst[i]==0 and lst[i]!=prvi:
                flag = False
        if flag:
            nedjeljivibr.append(prvi)
        duzina+=1
    return nedjeljivibr

        
listabr=[ 6, 2, 7, 9 ]

print(nedjeljivi(listabr))