"""
4.	Napisati funkciju koja prima niz brojeva i dodatni broj. Funkcija vraća 
rječnik koji će imati tri kljuca: ’vece’, ’manje’, ’jednako’. Vrijednost svakog 
kljuca je lista brojeva koji su veći, manji ili jednaki broju.
"""
def funk4(lst,N):
    rj={"vece":None,"manje":None,"jednako":None}
    vece=[]
    manje=[]
    jednako=[]
    for e in lst:
        if e>N and not e==N:
            vece.append(e)
        elif e<N and not e==N:
            manje.append(e)
        else:
            jednako.append(e)
    rj["vece"]=vece
    rj["manje"]=manje
    rj["jednako"]=jednako
    return rj

print(funk4([1,2,3,4,5,6,7,8,9,10],9))
    
                
                
