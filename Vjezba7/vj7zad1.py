import random
p=input("Da li je broj paran ili neparan? ")
a=random.randint(0,100)
def cijeli_broj(a):
    a = random.randint(0,100)
    if p == "Paran":
        a = random.randint(0,100)
        if a % 2 == 0:
            print(a)
        elif a % 2 == 1:
            print(a+1)
    else:
        a = random.randint(0,100)
        if a % 2 == 0:
            print(a-1)
        elif a % 2 == 1:
            print(a)
        
cijeli_broj(a)
            

            
        