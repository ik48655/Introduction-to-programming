def bitovi(a):
    if a < 2:
        return a
    else:
        return str (bitovi(a // 2)) + str (a % 2)
 
a=int(input("Unesite broj:"))
print ("Svi bitovi unesenog broja su:", bitovi(a))
