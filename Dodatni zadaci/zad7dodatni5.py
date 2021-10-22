def veca2(a,b):
    if a > b:
        return a
    else:
        return b
    
def veca5(c,d,e,f,g):
    cd=veca2(c,d)
    ef=veca2(e,f)
    cdef=veca2(cd,ef)
    return veca2 (cdef,g)

print(veca2(13,15))
print(veca5(5,16,17,23,11))