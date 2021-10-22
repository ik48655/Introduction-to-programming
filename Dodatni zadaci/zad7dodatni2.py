def funkcija2(a,b):
    br=0
    while a > 0 or b > 0:
        if a % 10 > b % 10:
            br+=1
        a=a//10
        b=b//10
    return br
print(funkcija2(98745,542387))
    