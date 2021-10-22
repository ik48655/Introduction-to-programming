#prosti faktori nekog broja
#funkcija koja provjerava je li broj prost

#provjera je li broj prost
def br_prost(n):
    if n < 2:
        return "Broj nije prost"
    else:
        if n == 2:
            return "Broj je prost"
        else:
            for i in range(2,n):
                if n % i == 0:
                    return "Broj nije prost"
            return "Broj je prost"

#prosti faktori nekog broja

def prosti_faktori(n):
    print(br_prost(n))
    
    