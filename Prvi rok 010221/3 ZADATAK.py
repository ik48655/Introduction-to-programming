"""
Napisati funkciju koja primljeni string rastavlja na niz stringova. Svaki
element u nizu ce biti dio originalnog stringa koji pocinje velikim slovom
i završava tockom.
"""

def rastavi(string):
    djelovirec=[]
    i_prije=0
    for i in range(len(string)-1):
        if string[i]=="." and string[i+1].isupper():
            diorec=string[i_prije:i+1]
            i_prije=i+1
            djelovirec.append(diorec)
    diorec=string[i_prije:]
    djelovirec.append(diorec)
    return djelovirec
        
    
print(rastavi("Ovo je.Recenica.koju.Treba rastaviti."))
print(rastavi("Ovo je.Recenica.koju.Treba rastaviti."))