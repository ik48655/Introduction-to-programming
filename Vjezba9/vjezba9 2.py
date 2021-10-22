#Napisati funkciju koja prima listu brojeva i vraća boolean. Funkcija vraća True samo ako su sve vrijednosti u listi poredane po veličini (rastući niz).

a=[1,2,3,5]

def funkc(a):
    b=True
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            b=False
            break
    return b 

print(funkc(a))   