"""
Napisati rekurzivnu funkciju djelitelji() koja ispisuje sve djelitelje broja
333.
"""
a=333
def djeljitelji(a):
    n=1
    while n <= 333:
        if a % n == 0:
            print("Djeljitelji broja 333 su: ",n)
        n=n+1
        
djeljitelji(a)
        
