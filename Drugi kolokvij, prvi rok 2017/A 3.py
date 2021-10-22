"""
Napisati funkciju koja prima paran broj N i vraca matricu velicine NxN
ispunjenu sa jedinicama i nulama. Gornja polovica matrice je ispunjena
jedinicama.
"""
def funkya3(N):
    matrix=[]
    for i in range(N):
        redak=[]
        for j in range(N):
            if i<(N/2):
                redak.append(1)
            else:
                redak.append(0)
        matrix.append(redak)
    return matrix

matrica=funkya3(8)
for red in matrica:
    print(red)

    