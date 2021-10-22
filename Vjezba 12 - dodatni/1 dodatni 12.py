"""
1.	Napisati funkciju koja prima string i vraća novi string koji nastaje tako 
da se iz primljenog stringa izbace svi zarezi.
"""

def funk(string):
    string3=""
    string2=string.split(",")
    for i in string2:
        string3="".join(string2)
    return string3
    
string1="1,2,3,4,5,6,7,8"

print(funk(string1))
        