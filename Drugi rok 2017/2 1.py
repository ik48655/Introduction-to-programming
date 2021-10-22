"""
Napisati funkciju koja prima listu brojeva. Funkcija ce vratiti dvije liste
koje ce sadržati parne i neparne brojeve iz primljene liste.
"""

def funky1(lst):
    par=[]
    nepar=[]
    for i in lst:
        if i%2==0 or i==0:
            par.append(i)
        else:
            nepar.append(i)
    return par,nepar

print(funky1([1,2,3,4,5,6,123,6,-5,3,3,7,0]))
            