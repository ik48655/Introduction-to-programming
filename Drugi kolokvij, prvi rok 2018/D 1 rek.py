#rekurzivna funkcija za djeljitelje broja 333/555
def djeljitelji(broj,a):
    while a<=broj:
        if broj%a==0:
            print(a)
            return djeljitelji(broj,a+1)
        else:
            return djeljitelji(broj,a+1)
            
djeljitelji(555,1)
        