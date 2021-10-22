"""
Napisati funkciju koja prima listu brojeva i ispisuje samo elemente na
parnim indeksima.
"""

def funkyd1(lst):
    for e in range(len(lst)):
        if e%2==0:
            print(lst[e])

lstbr=[1,2,3,4,5,6,7,8,9,10]
lstbr2=[1,2,3,4,5]
lstbr3=[6,7,8,9,10]
lstbr4=[10]

funkyd1(lstbr)
funkyd1(lstbr2)
funkyd1(lstbr3)
funkyd1(lstbr4)