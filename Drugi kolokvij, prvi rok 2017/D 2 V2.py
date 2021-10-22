"""
Napisati funkciju koja prima string i vraca novi string koji nastaje tako
da se iz primljenog stringa izbace svi zarezi.
"""

def funkyTea(string):
    string2=""
    bezzareza=string.split(",")
    for i in bezzareza:
        string2+=i
    return string2

print(funkyTea("1,2,3,4,5,6,7"))
print(funkyTea("1,2,,,3,4,5,6,7"))
print(funkyTea("1,2,3,4,5,6,7,"))