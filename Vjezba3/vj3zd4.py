#a
x=5
y=3
print(int((x/2)+(y/2)))
#moramo ispisati rezultat djeljenja kao integer da dobijemo rezultat 4 a ne 4.0

#b
x=5
y=x+5
print((x+y)%2)
#izraz (x+y) moramo staviti u zagradu da bi dobili ostatak djeljenja 15%2 =  1

       
#c
x=1234
x = x // 1000
print(x)
x = 1234 % 1000 // 100
print(x)
x = 1234 % 100 // 10
print(x)
x = 1234 % 10
print(x)
#objasnjenje: x // 1000 nam daje uvijek 1 od 1.234;
#1234%1000//100 daje vrijednost 2 jer 1234%1000 je 234 i 234//100 je 2;
#1234%100 je 34 i 34//10 je 3.4 odnosno 3
#1234 % 10 je 4 jer djeljenjem dobijemo 123.4 a ostatak je 4
