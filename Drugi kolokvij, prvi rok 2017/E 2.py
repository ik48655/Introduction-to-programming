"""
Napisati funkciju koja prima dva stringa i broj N. Funkcija vraca true ako
prvi string sadrži N samoglasnika, a drugi string N suglasnika. Npr. za
stringove „uzeti“, „abcde“ i N=3, funkcija vraca True.
"""

def funkye2(string1,string2,N):
    samogl=0
    sugl=0
    for c in string1:
        if c in "AEIOUaeiou":
            samogl=samogl+1
    for c in string2:
        if c not in "AEIOUaeiou":
            sugl=sugl+1
    if samogl and sugl == N:
        return True
    else:
        return False
    
    
str1="uzeti"
str2="abcde"
print(funkye2(str1,str2,3))

str3="brod"
str4="ivo"
print(funkye2(str3,str4,1))

str5="jabuka"
str6="drvo"
print(funkye2(str5,str6,3))

str7="aeiou"
str8="cvrst"
print(funkye2(str7,str8,5))

            
        
        