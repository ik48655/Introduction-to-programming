#Napisati funkciju koja prima dvije liste brojeva i koja ispisuje brojeve iz prve liste koji su djeljivi sa 3, a ujedno se nalaze i u drugoj listi.

lista1=[1,2,3,4,9]
lista2=[2,3,4,5,9]

def funkc(lista1,lista2):
    for i in range(len(lista1)):
        if lista1[i]%3==0:
            if lista1[i] in lista2:
                print(lista1[i])
funkc(lista1,lista2)  