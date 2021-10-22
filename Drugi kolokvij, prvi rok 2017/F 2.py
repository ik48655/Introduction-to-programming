"""
Napisati funkciju koja prima string sastavljen od malih slova. Funkcija
vraca string gdje su svi dvostruki suglasnici zamijenjeni jednim suglasnikom.
Npr. za string "lookk", funkcija ce vratiti "look".
"""

def dvasugl(string1):
    samoglasnici=["a","e","i","o","u"]
    string2=string1[0]
    skip = False
    for c in string1[1:]:
        if c != string2[-1] or c in samoglasnici:
            string2 += c
            skip = False
        elif c == string2[-1] and c not in samoglasnici and not skip:
            skip = True
        else:
            string2 += c
            skip = False
    return string2

print(dvasugl("llookk"))
print(dvasugl("lookk"))
print(dvasugl("llookkk"))
