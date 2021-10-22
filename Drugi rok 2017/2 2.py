"""
Napisati funkciju koja prima string i vraca novi string koji nastaje tako
da se iz primljenog stringa izbace svi zarezi.
"""

def funky2(string):
    string2=""
    bezzareza=string.split(",")
    for i in bezzareza:
        string2=string2+i
    return string2


print(funky2("a,b,c,1,2,3,4,c,+,-,1"))
        