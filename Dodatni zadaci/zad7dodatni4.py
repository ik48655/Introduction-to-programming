def funkcija4(a,b):
    if a==0:
        return 0
    if a%10 != b%10:
        return 1 + funkcija4(a//10,b//10)
    else:
        return 0 + funkcija4(a//10,b//10)
    
print(funkcija4(36415,32816))