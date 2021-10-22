"""
Napisati funkciju koja prima dva stringa sastavljena od cijelih pozitivnih
brojeva odvojenih zarezom. Oba stringa sadrže isti broj brojeva. Funkcija
vraca string (istog formata) gdje su elementi zbroj dva broja iz prvog i
drugog stringa. Npr. za „3,14,2,10“ i „6,11,5,5“, funkcija vraca „9,25,7,15“.
"""

def odvojizbroji(string1,string2):
    djelovi1=string1.split(",")
    djelovi2=string2.split(",")
    zbroj=[]
    for i in range(len(djelovi1)):
        zbroj2=int(djelovi1[i] ) + int(djelovi2[i])
        zbroj.append(str(zbroj2))
    print(",".join(zbroj))
        
odvojizbroji("1,2,3,4,5","6,7,8,9,10")
        