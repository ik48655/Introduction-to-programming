a=0
b=int(input("Unesi broj: "))
for i in range (32):
    if b & 1==1:
        a=a+1
    b= b >> 1
print(a)     
     