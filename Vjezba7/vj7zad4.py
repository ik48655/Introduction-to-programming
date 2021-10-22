"""
Napisati rekurzivnu funkciju koja prima kao 
parametar pozitivan cijeli broj i vraća zbroj svih parnih
brojeva do tog broja.
"""

def zbr_par(x):
    if x % 2 == 1:
        x = x - 1
    if x == 0:
        return 0
    return x + zbr_par(x-2)

x=int(input("Unesite neki broj:"))
print("Zbroj svih parnih brojeva uključujući unos je:", zbr_par(x))

def zbr_par_bez_unosa(y):
    if y==0:
        return y
    if y%2==0:
        return((y-2)+zbr_par_bez_unosa(y-2))
    if y%2!=0:
        return((y-1)+zbr_par_bez_unosa(y-1))
    
x=int(input("Unesite neki broj:"))
print("Zbroj svih parnih brojeva ne uključujući unos je :", zbr_par_bez_unosa(x))