unos=int(input("Unesi početni broj: "))
zbroj=0
while unos>0:
    if unos & 1 == 0:
        unos=unos>>1
    else:
        unos2=int(input("Unesite još jedan broj:"))
        zbroj=zbroj+unos+unos2
        unos=unos >> 1
        
print("Zbroj je: ", zbroj)