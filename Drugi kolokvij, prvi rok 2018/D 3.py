"""
Napisati funkciju koja prima listu stringova i vraca novu listu stringova. U
novu listu se dodaju samo stringovi koji su ispravni e-mailovi po formatu
’ime.prezime@unist.hr’, gdje su ime i prezime dugi do 10 znakova.
"""

def emailovi(lst):
    ok_emailovi=[]
    for e in lst:
        prvdio=e.split("@")
        if len(prvdio) == 2 and prvdio[1] == "unist.hr":
            ime_prez=prvdio[0].split(".")
            flag=True
        else:
            flag=False
        if flag and (len(ime_prez[0])+len(ime_prez[1])) == 10:
            if ime_prez[0].isalpha() and ime_prez[1].isalpha:
                ok_emailovi.append(e)
    return ok_emailovi
        
        
        
poc_email=["ime.prezime@unist.hr",
          "ime1.pr3zime@unist.hr",
          "ime.prez@unist.hr",
          "ime.prezime@oss.unist.hr",
          "ime.prezime@unist.hr",
          "Ime.Prezime@unist.hr"
    ]

print(emailovi(poc_email))