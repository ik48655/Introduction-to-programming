def funkcija6(a,b):
    if a > b:
        a,b = b,a
    if a==b-1:
        return 0
    return a+1 + funkcija6(a+1,b)

print(funkcija6(3,7))
    