"""
Napisati funkciju koja prima dvije liste brojeva. Funkcija vraca listu sa
brojevima koji se pojavljuju u prvoj, ali ne i u drugoj listi. Npr. za liste 
[6, 2, 7, 9 ] i [2, 4, 5, 7], funkcija vraca listu [6, 9].
"""
def funky(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i not in lst2:
            lst3.append(i)
    return lst3

print(funky([6,2,7,9],[2,4,5,7]))
            