#Napisati funkciju koja prima string i vraća novi string koji nastaje tako da se iz primljenog stringa izbace svi zarezi.

string="b,3,acb,uwu,sh,*,a,c,"

def f(x):
    y=""
    for slovo in x:
        if slovo!=",":
            y+=slovo
    return y
print(f(string))