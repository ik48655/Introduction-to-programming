#Napisati funkciju koja prima listu brojeva i ispisuje samo parne elemente. Napisati drugu funkciju koja prima listu brojeva i ispisuje samo elemente na parnim indeksima.

lista=[1,2,3,4,25,39,44,69,420]

def funkc(n):
    for i in range (len(lista)):
        if lista[i]%2==0:
         print(lista[i])
def funkc2(k):
    for i in range(len(lista)):
        if i%2==0 and i!=0:
            print(lista[i])

print("parni brojevi iz liste: ")
funkc(lista)
print("Parni indexi iz liste: ") 
funkc2(lista)