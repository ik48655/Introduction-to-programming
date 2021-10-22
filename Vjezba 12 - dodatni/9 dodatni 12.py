"""
9.	Napisati funkciju koja prima listu brojeva i listu stringova. Funkcija 
ispisuje samo stringove na indeksima zadanim u listi brojeva.
"""

def funky9(lst1,lst2):
    for i in lst1:
        if i >= 0 and i < len(lst2):
            print(lst2[i])
        
        
listabr=[1,3,5,7,0]
listastr=["nulti","prvi","drugi","treci","cetvrti","peti","sesti","sedmi","osmi","deveti","deseti"]

funky9(listabr,listastr)