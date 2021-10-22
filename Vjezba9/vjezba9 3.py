#Napisati funkciju koja prima listu brojeva i vraća dva booleana. Prvi boolean je True samo ako su sve vrijednosti u listi jednake, drugi boolean je True samo ako su barem dvije vrijednosti u listi jednake.

lista=[1,1,2,3,4]

def funkc(lista2):
    a=1
    b=0
    for i in range(0,len(lista2)-1):
        if lista2[1]!=lista2[i]:
            a=0
            
        
    for i in range(1,len(lista2)):
        if lista2[i-1]==lista[i]:
            b=1
    if a==1 and b==1:
        return True,True
    elif a==0 and b==1:
        return False,True
    elif a==1 and b==0:
        return True,True
    else:
        return False,False

print(funkc(lista))