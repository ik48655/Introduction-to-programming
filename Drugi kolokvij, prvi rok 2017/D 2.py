"""
Napisati funkciju koja prima string i vraca novi string koji nastaje tako
da se iz primljenog stringa izbace svi zarezi.
"""

def funkyd2(string):
    bezzareza=string.split(",")
    #print(bezzareza)
    print("".join(bezzareza)) 
    
funkyd2("1,2,3,4,5,6,7")
funkyd2("1,2,,,3,4,5,6,7")
funkyd2("1,2,3,4,5,6,7,")