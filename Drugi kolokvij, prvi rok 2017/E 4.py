"""
Napisati funkciju koja prima listu lista brojeva. Funkcija od brojeva u
listi konstruira rjecnik koji kao kljuceve ima najveci broj iz svake pojedine
liste, a svakom kljucu je kao vrijednost pridružena ta lista.
"""

def funkye4(matrix):
    rjecnik={}
    for e in matrix:
        najv=e[0]
        for i in e:
            if i>najv:
                najv=i
        k=najv
        rjecnik[k]=e
    return rjecnik

lista1=[[1,2,3],[4,5,6],[7,8,9]]
print(funkye4(lista1))
            
            
