#Napisati funkciju koja prima listu stringova i vraca novu listu stringova. U novu listu se dodaju samo
#stringovi koji su ispravni e-mailovi po formatu 'ime.prezime@unist.hr', gdje su ime i prezime dugi do
#10 znakova.

def vracastring(lista):
    nova=[]
    for e in lista:
        djelovi= e.split('@')
        print(len(djelovi))
        if len(djelovi)==2 and djelovi[1] =="unist.hr":
               prvi_djelovi = djelovi[0].split(".")
               flag=True
        else:
            flag=False
        if flag and (len(prvi_djelovi[0]) <10 and len(prvi_djelovi[1]) <10 ):
            if (prvi_djelovi[0].isalpha() and prvi_djelovi[1].isalpha()):
                nova.append(e)
    return nova

lista=[ "imeduze.prezime@unist.hr", "imeprezime@unist.hr", "ime7.prezime@unist.hr", "ime.prezime@unist.hr",
      "ime.prezime@@oss.unist.hr", "ime.prezime@oss@unist.hr", "ime.prezimeosss.unist.hr"
      "imeeeeeeeeeee.prezim@unist.hr" ]
print(len(lista))
print(vracastring(lista))