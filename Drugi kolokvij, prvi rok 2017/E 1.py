"""
Napisati funkciju koja prima listu brojeva i listu booleana jednake dužine.
Lista booleana ima tocno dva elementa postavljena na True. Ta dva elementa
oznacavaju pocetak i kraj liste brojeva koju funkcija treba „izbaciti“
iz originalne liste (funkcija vraca novu listu). Na primjer, za liste [ 6, 2,
8, 4, 9 ] i [ F, T, F, T, F ], funkcija vraca listu [ 6, 9 ].
"""

def funkye1(lst1,lst2):
    nova=[]
    brojac=0
    for i,e in enumerate(lst2):
        if e == True:
            brojac=brojac+1
        if brojac==0:
            nova.append(lst1[i])
        if brojac==2 and e==False:
            nova.append(lst1[i])
    return nova


listabr=[6,2,8,4,9]
listabool=[False,True,False,True,False]
print(funkye1(listabr,listabool))
listabr2=[6,2,8,4,9]
listabool2=[False,True,True,False,False]
print(funkye1(listabr2,listabool2))
