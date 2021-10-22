a=float(input("Unesite neki broj: "))
b=float(input("Unesite neki broj: "))
c=float(input("Unesite neki broj: "))

def sr_br(a,b,c):
    if a > b:
        if a < c:
            print("Srednji broj je: ", a)
        elif b > c:
            print("Srednji broj je: ", b)
        else:
            print("Srednji broj je: ", c)
    else:
        if a > c:
            print("Srednji broj je: ", a)
        elif b < c:
            print("Srednji broj je: ", b)
        else:
            print("Srednji broj je: ", c)
            
sr_br(a,b,c)
            
    
    