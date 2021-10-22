"""
Napisati funkciju koja prima niz brojeva. Funkcija vraca
rjecnik koji ce imati tri kljuca: ’parni’, ’neparni’, ’nule’. Vrijednost svakog
kljuca je lista brojeva koji su parni, neparni ili nula.
"""

def parneparnula(lst):
    rjecnik={"par":None,"nepar":None,"nula":None}
    parni=[]
    neparni=[]
    nule=[]
    for e in lst:
        if e%2==0 and e!=0:
            parni.append(e)
        elif e%2==1:
            neparni.append(e)
        else:
            nule.append(e)
            
    rjecnik["par"]=parni
    rjecnik["nepar"]=neparni
    rjecnik["nula"]=nule
    
    return rjecnik

print(parneparnula([0,1,2,3,4,5,6,7,8,9,10,0,0]))
            