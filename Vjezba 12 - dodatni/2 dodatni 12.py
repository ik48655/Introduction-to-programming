"""
2.	Napisati funkciju koja prima dvije liste brojeva. Funkcija vraća listu sa 
brojevima koji se pojavljuju u prvoj, ali ne i u drugoj listi. Npr. za liste 
[ 6, 2, 7, 9 ] i [2, 4, 5, 7], funkcija vraća listu [6, 9].   
"""

def funk2(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i not in lst2:
            lst3.append(i)
    return lst3


lista1=[6,2,7,9]
lista2=[2,4,5,7]

print(funk2(lista1,lista2))
            
            
            