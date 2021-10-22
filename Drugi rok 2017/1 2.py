"""
Napisati funkciju koja prima string sastavljen od cijelih pozitivnih i negativnih
brojeva odvojenih razmakom. Funkcija vraca par stringova istog
formata (brojevi odvojeni zarezom). Prvi string sadrži samo pozitivne, a
drugi samo negativne brojeve iz originalnog stringa.
"""

def pozneg(string):
    poz=[]
    neg=[]
    nule=[]
    rastavljeni=string.split(" ")
    for i in range(len(rastavljeni)):
        if int(rastavljeni[i])>0:
            poz.append(rastavljeni[i])
        elif int(rastavljeni[i])==0:
            nule.append(rastavljeni[i])
        else:
            neg.append(rastavljeni[i])
    return ",".join(poz),",".join(neg)

print(pozneg("1 -2 3 -4 5 -6 7 -8 9 -10"))
print(pozneg("1 -1 1 -1 -1 -1 1 2 -3 1 0"))
print(pozneg("0 1 0 1 -2 0 1 0 1 0"))
print(pozneg("2 4 2 4 2 -1"))
            
    