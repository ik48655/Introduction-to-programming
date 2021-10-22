"""
Napisati funkciju koja prima jedan string. String može biti „X plus Y“ ili
„X minus Y“, gdje su X i Y dva cijela broja (mogu imati više znamenki
ili predznak). Funkcija vraca zbroj ili razliku brojeva X i Y.
"""

def funkyb2(string1):
    lista=string1.split(" ")
    x=int(lista[0])
    y=int(lista[2])
    if "plus" in lista:
        return x + y 
    elif "minus" in lista:
        return x -y 
    else:
        return "String ne sadrži plus ili minus!"
    
        
print(funkyb2("-10 plus 11"))
print(funkyb2("10 minus -11"))
print(funkyb2("1000 minus 111"))
print(funkyb2("10 mnozi 11"))

        
        