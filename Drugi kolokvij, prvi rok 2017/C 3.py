"""
Napisati funkciju koja primljeni string rastavlja na niz stringova. Svaki
element u nizu ce biti dio originalnog stringa koji pocinje otvorenom i
završava zatvorenom zagradom. Npr. za string "ab(cd)ef(g)", funkcija
vraca [ "cd", "g" ].
"""
def rastav(string):
    djelovi=[]
    poc=-1
    cilj=-1
    for i in range(len(string)):
        if string[i] == "(":
            poc=i+1
        elif string[i] == ")":
            cilj = i-1
            djelovi.append(string[poc:cilj+1])
    return djelovi

print(rastav("ab(cd)ef(g)"))