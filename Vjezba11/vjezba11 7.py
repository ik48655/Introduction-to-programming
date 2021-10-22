#Napisati program koji telefonski broj tipa 0800-CALL-ME pretvara u telefonski broj sastavljen samo od
#znamenki i povlaka. Pretvaranje se vrši uz pomoć rječnika koji za svako slovo definira odgovarajuću
#znamenku (slovima 'a', 'b' i 'c' odgovara znamenka 1, ...)

stari_broj = input("Unesite broj telefona: ")
novi_broj = ""
rijecnik = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
            "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20,
            "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
for e in stari_broj:
    if e.isalpha():
        slovo = e.lower()
        novi_broj += str(rijecnik[slovo])
    else:
        novi_broj += str(e)
        
print(novi_broj)