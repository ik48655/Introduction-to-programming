"""
Napisati funkciju koja prima listu brojeva i listu stringova. Funkcija
ispisuje samo stringove na indeksima zadanim u listi brojeva.
"""

def funky(lstbr,lststr):
    for i in lstbr:
        if (i>=0 or i<=0) and i<len(lststr):
            print(lststr[i])
        
funky([0,2,4,-4,-5],["abc","def","ghi","jkl","mno"])