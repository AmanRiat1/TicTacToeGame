def add(x):
    '''
    d = -1
    for y in range(len(x)):
        d += 1
        for z in (x[d]):
            z += 1
            print (z)
    return x
    '''


def add_V2(y):
    new = y.copy()
    a = []
    z = (len(y))
    for d in range(0,z):
        b = [a + 1 for a in new[d]]
        a.append(b)
    return a
        
z = [[2, 3, 4], [5, 6, 7],[8,9,10]]
print (add_V2(z))

#Main


