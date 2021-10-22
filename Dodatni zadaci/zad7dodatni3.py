def funkcija3():
    a1=int(input("Unesite broj a: "))
    b1=int(input("Unesite broj b: "))
    while True:
        a2=int(input("Unesite broj a: "))
        b2=int(input("Unesite broj b: "))
        if a2>a1 and b2>b1:
            return(a2,b2)
        
print(funkcija3())