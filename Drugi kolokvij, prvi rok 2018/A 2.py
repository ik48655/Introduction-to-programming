"""
Napisati funkciju koja prima jedan string i broj. Funkcija vraca True ako
se broj nalazi negdje u stringu tocno jednom. Npr. za string „parni broj
42“ i broj 42, funkcija vraca True, a za „10 plus 10“ i 10 vraca False.
"""

def brojustr(string,n):
    brojac=0
    djelovi_stringa=string.split(" ")
    for e in djelovi_stringa:
        if str(n) in e:
            brojac=+1
        if brojac==1:
            return True
        else:
            return False
        
print(brojustr("10 broj 10",10))
print(brojustr("parni broj 42",42))
        