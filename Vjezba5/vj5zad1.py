import random
a=0
while(a<10):
    x=random.randint(0, 1001)
    if x >= 100 and x <= 500:
        a=a+1
        print(x)