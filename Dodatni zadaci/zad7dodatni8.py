s=int(input("Unesi broj: "))
for i in range(s):
    for n in range(s):
        if n==0 and i<(s//2):
            print("#",end=' ')
        elif n==(s-1) and i>(s//2):
            print("#",end=' ')
        elif i==0 or i==(s//2) or i==(s-1):
            print("#",end=' ')
        else:
            print(" ",end=' ')
    print()