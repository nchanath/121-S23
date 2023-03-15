def createRational(n,d):
    return [n,d]

def numerator(r):
    return r[0]

def denominator(r):
    return r[1]

def rationalProduct(r,s):
    newNumer = numerator(r) * numerator(s)
    newDenom = denominator(r) * denominator(s)
    return createRational(newNumer, newDenom)

def rationalSum(r,s):
    nr,dr = numerator(r), denominator(r)
    ns,ds = numerator(s), denominator(s)
    newNumer = nr*ds + ns*dr
    newDenom = ds*dr
    return createRational(newNumer, newDenom)

def areSameRationals(r,s):
    nr,dr = numerator(r), denominator(r)
    ns,ds = numerator(s), denominator(s)
    return (nr*ds == ns*dr)

def stringOfRational(r):
    ntext = str(numerator(r))
    dtext = str(denominator(r))
    return ntext + "/" + dtext

def outputRational(r):
    print(stringOfRational(r))

def rationalSubtraction(r,s):
    nr,dr = numerator(r), denominator(r)
    ns,ds = numerator(s), denominator(s)
    newNumer = (nr*ds) - (ns*dr)
    newDenom = dr*ds
    return createRational(newNumer, newDenom)

def rationalDivision(r,s):
    return
