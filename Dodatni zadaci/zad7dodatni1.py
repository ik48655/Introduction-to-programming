def funkcija1():
    while True:
        a=int(input("Unesite broj a: "))
        b=int(input("Unesite broj b: "))
        if (a<0 and b>0) or (a>0 and b<0):
            return(a,b)
print(funkcija1())
             