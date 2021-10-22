a = input("Unesite neki broj ")
b = input("Unesite neki broj ")
c = input("Unesite neki broj ")
if a > b and a > c:
    if b > c:
        print(a,b,c)
    elif b < c:
        print(a,c,b)
        
elif b > a and b > c:
    if a > c:
        print(b,a,c)
