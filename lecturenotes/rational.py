def createRational(n,d):
    return [n,d]

def numerator(r):
    return r[0]

def denomitator(r):
    return r[1]

def rationalProduct(r,s):
    newNumer = numerator(r) * numerator(s)
    newDenom = denomitator(r) * denomitator(s)
    return createRational(newNumer, NewDenom)

def rationalSum(r,s):
    nr,dr = numerator(r), denomitator(r)
    ns,ds = numerator(s) * denomitator(s)
    newNumer = nr*ds + ns*dr
    newdenom = ds*dr
    return createRational(newNumer, NewDenom)

def areSameRationals(r,s):
    nr,dr = numerator(r), denomitator(r)
    ns,ds = numerator(s), denomitator(s)
    return (nr*ds == ns*dr)

def stringOfRational(r):
    ntext = str(numerator(r))
    dtext = str(denomitator(r))
    return ntext + "/" + dtext

def outputRational(r):
    print(stringOfRational(r))

def rationalSubtraction(r,s):
    return

def rationalDivision(r,s):
    return
