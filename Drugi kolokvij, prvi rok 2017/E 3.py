"""
Napisati funkciju koja prima matricu (listu lista) i vraca listu sastavljenu
od svih brojeva u matrici.
"""

def funkye3(matrix):
    brojevi=[]
    for e in matrix:
        for elem in e:
            brojevi.append(elem)
    return brojevi
    
    
matrica=[
         [2,0,5],
         [6,6,6],
         [3,6,7],
         [8,9,1]
        ]

print(funkye3(matrica))