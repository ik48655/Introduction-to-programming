"""
Napisati funkciju koja prima listu lista (matricu) brojeva. Funkcija od brojeva u
listi konstruira rjecnik koji kao kljuceve ima najveci broj iz svake pojedine
liste, a svakom kljucu je kao vrijednost pridružena ta lista.
"""

def najv_v(lst):
    rjecnik={}
    for e in lst:
        najv=e[0]
        for i in e:
            if i > najv:
                najv = i
        k = najv
        rjecnik[k] = e
    return rjecnik

list_bro=[
         [1,2,3],
         [4,5,6],
         [7,8,9],
         [10,11,12],
         [13,14,15],
        ]

print(najv_v(list_bro))


