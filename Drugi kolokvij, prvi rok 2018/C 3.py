"""
Napisati funkciju koja prima paran broj N i vraca matricu velicine NxN
ispunjenu sa jedinicama i nulama. Gornja polovica matrice je ispunjena
jedinicama.
"""

def matrixN(N):
    matrica=[]
    for r in range(N):
        redak=[]
        for s in range(N):
            if r<(N//2):
                redak.append(1)
            else:
                redak.append(0)
        matrica.append(redak)
    return matrica
m=matrixN(8)
for r in m:
    print(r)
    
    
print(matrixN(8))
                
                
                
                
