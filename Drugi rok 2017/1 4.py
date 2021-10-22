"""
Napisati funkciju koja prima listu brojeva i dva broja M i N. Funkcija od
brojeva u listi konstruira matricu velicine MxN i vraca je.
"""

def funky4(lst,M,N):
    matrix=[]
    for r in range(M):
        redak=[]
        for s in range(N):
            if len(lst)-1 < s:
                redak.append(0)
            else:
                redak.append(lst[s])
        matrix.append(redak)
    return matrix

mnlst=funky4([1,2,3,4],5,10)
for j in mnlst:
    print(j)
                