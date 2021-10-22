"""
Napisati rekurzivnu funkciju koja vraca zbroj svih znamenaka broja.
"""

def rekurz(number):
  if number == 0:
    return 0
  else:
    return (number%10) + rekurz(number//10)
        
print(rekurz(1234))
print(rekurz(5678))
print(rekurz(9101))
        