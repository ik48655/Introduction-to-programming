while(True):
    x=int(input("Unesi prvi broj: "))
    y=int(input("Unesi drugi broj: "))
   
    if x>0 and y>0 and x<y:
       
       for a in range(x,y):
           print(a)    
            
    else:
        print("Greška")
        break