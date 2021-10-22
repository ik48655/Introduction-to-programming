"""
Napisati program koji zvjezdicama iscrtava prazan pravokutni trokut (katete
su postavljene kao L). Katete su jednake dužine, zadane od korisnika. Zadatak
rješiti petljama i pomocnom funkcijom za iscrtavanje N razmaka
(napisati funkciju).
"""
def trokut(n):
    for row in range(n):
        for col in range(n):
            if col==0 or row==(n-1) or row==col:
                print("#",end=" ")
            else:
                print(end="  ")
        print()
    print()
    
n=int(input("Unesite broj redaka: "))
trokut(n)  