"""
Napisati funkciju koja primljeni string rastavlja na niz stringova. Svaki
element u nizu ce biti dio originalnog stringa koji pocinje velikim slovom
i završava tockom.
"""

def rastav2(string):
    djelovi=[]
    poc=-1
    cilj=-1
    for i in range(len(string)):
        if string[i].isupper():
            poc=i+1
        elif string[i] == ".":
            cilj = i-1
            djelovi.append(string[poc-1:cilj+1])
    return djelovi


print(rastav2("Ovo. je.Recenica koju.Treba isjeci."))