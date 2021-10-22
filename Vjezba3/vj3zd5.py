#a
a=1
b=-1
if a > 0 and b > 0:
    print("True")
else:
    print("False")
#b
a=2
b=4
if a % 2 == 0 and b % 2 == 0:
    print("True")
else:
    print("False")
#c
a=8
b=3
if a % 2 == 0 and b % 2 == 0 and a > b:
    print("True")
else:
    print("False")
#d
a=3
b=4
if a % 2 == 1 or b % 2 == 1:
    print("True")
else:
    print("False")
#e
a = 3
b = 3
if a % 2 == 1 and b % 2 == 1:
    print("False")
    
elif a % 2 == 1 or b % 2 == 1:
    print("True")
    
elif a % 2 == 0 or b % 2 == 0:
    print("False")
#f
a=6
b=6
c = a/b
d = b/a
if a / b == c and b / a == d:
    print("True")
else:
    print("False")
#g
a=0
b=6
c = a/b
d = b/a
if (a / b) == c and (b / a) == d:
    print("True")
else:
    print("False")
