"""
7.	Napisati funkciju koja prima broj N i vraća dijagonalnu matricu veličine NxN.
"""

def matrix(N):
    matrix=[]
    for i in range(N):
        redak=[]
        for j in range(N):
            if i==j:
                redak.append(1)
            else:
                redak.append(0)
        matrix.append(redak)
    return matrix

N = int(input("Unesite zeljenu velicinu matrice: "))

mat=matrix(N)

for red in mat:
    print(red)