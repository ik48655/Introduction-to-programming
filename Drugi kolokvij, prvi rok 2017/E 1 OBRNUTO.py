"""
Napisati funkciju koja prima listu brojeva i listu booleana iste duzine.
Lista booleana ima tocno dva elementa postavljena na True. Ta dva elemeneta oznacavaju
poceetak i kraj liste brojeva koju funkcija treba vratiti. Na primjer, za liste
[6,2,8,4,9] i [F,F,T,F,T] funkcija vraca listu [8,4,9]
"""

def funkye12(lst1,lst2):
    nova=[]
    brojac=0
    for i in range(len(lst2)):
        if lst2[i]==True:
            brojac+=1
        if brojac == 1 or (brojac<=2 and lst2[i]==True):
            nova.append(lst1[i])
    return nova

listabr=[6,2,8,4,9]
listabool=[False,False,True,False,True]
print(funkye12(listabr,listabool))
listabr2=[6,2,8,4,9]
listabool2=[True,False,True,False,False]
print(funkye12(listabr2,listabool2))
    