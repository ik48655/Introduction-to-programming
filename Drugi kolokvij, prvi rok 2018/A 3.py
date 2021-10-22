"""
Napisati funkciju koja prima matricu (listu redaka) i vraca listu sastavljenu
od prvog broja svakog retka matrice.
"""

def frstmemb(lst):
    listabr2=[]
    for e in lst:
        privr=e[0]
        listabr2.append(privr)
    return listabr2
    
listabr=[[1,2,3],
         [4,5,6],
         [7,8,9]]

print(frstmemb(listabr))