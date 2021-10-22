#Napisati program koji od korisnika čita brojeve i sprema ih u listu. Kada korisnik upiše 0, program pita
#za dodatni broj N i ispisuje zbroj zadnjih N upisanih brojeva. Ako u listi nema dovoljno brojeva, program
#ispisuje grešku i završava.

lista_brojeva = []
while True:
    broj = int(input("unesite broj: "))
    lista_brojeva.append(broj)
    if broj == 0:
        N = int(input("Unesite dodatni broj: "))
        if N > (len(list)):
            print("Greska")
            break
        while N>0:
            print(list[-N])
            N -= 1
        if N==0:
            break