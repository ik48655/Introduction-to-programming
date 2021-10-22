"""
8.	Napisati funkciju koja prima jedan string i dva broja A i B. Funkcija vraća
 true ako prvi string sadrži A samoglasnika i B suglasnika. Npr. za string
 „ab cd e“, A=2 i B=3, funkcija vraca True.
"""

def funky8(string1,a,b):
    samoglasnici=["a","e","i","o","u","A","E","I","O","U"]
    brsugl=0
    brsamogl=0
    for c in string1:
        if c in samoglasnici:
            brsamogl=brsamogl+1
        elif c.isalpha() and c not in samoglasnici:
            brsugl=brsugl+1
    if brsamogl == a and brsugl == b:
        return True
    return False

print(funky8("ab cd e",2,3))
print(funky8("olovo",3,1))
print(funky8("jabuka",3,6))
print(funky8("do re mi fa so la ti do",8,8))
        