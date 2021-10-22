"""
Napisati funkciju koja prima dva stringa i broj N. Funkcija vraca true ako
prvi string sadrži N samoglasnika, a drugi string N suglasnika. Npr. za
stringove „uzeti“, „abcde“ i N=3, funkcija vraca True.
"""

def funkya2(string1,string2,N):
    samogl=0
    sugl=0
    for c in string1: #redundantna linija koda
        if c in "AEIOUaeiou": #ne provjerava da li je unešen neki znak, treba staviti .isalpha()
            samogl=samogl+1
    for c in string2: #redundantna linija koda
        if c not in "AEIOUaeiou": #ne provjerava da li je unešen neki znak, treba staviti .isalpha(), ako se unese znak zbraja ga u suglasnike
            sugl=sugl+1
    if samogl and sugl == N:
        return True
    else:
        return False


print(funkya2("uzeti","abcde",3))
            