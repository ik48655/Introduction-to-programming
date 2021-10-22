#Napisati funkciju koja prima dvije liste brojeva i koja računa srednju vrijednost brojeva prve liste, a ispisuje brojeve iz druge liste koji su veći od izračunane srednje vrijednosti.

def funkc(lista1,lista2):
    x=0
    for i in lista1:
        x+=i
    y=x/len(lista1)
    for i in lista2:
        if i>y:
            print(i)
        
        
lista1=[1,2,3,4,5,6,7,8,9,10,11]
lista2=[2,4,7,9,11]
funkc(lista1,lista2)