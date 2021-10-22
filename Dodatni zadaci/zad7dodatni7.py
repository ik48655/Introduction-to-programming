def rekurzivna(broj):
    if broj==0:
        return 
    print(broj%10)
    rekurzivna(broj//10)
        
rekurzivna(12345)