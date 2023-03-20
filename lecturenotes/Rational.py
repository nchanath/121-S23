from math import gcd

class Rational:
    
    def __init__(self,n,d):
        if d < 0:
            n *= -1
            d *= -1
        g = gcd(n,d)
        self.numerator = n // g
        self.denominator = d // g

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def times(self,other):
        sn = self.getNumerator()
        sd = self.getDenominator()
        on = other.getNumerator()
        od = other.getDenominator()
        return Rational(sn*on, sd*od)

    def plus(self,other):
        sn = self.getNumerator()
        sd = self.getDenominator()
        on = other.getNumerator()
        od = other.getDenominator()
        return Rational(sn*od + on*sd, sd*od)

    def __eq__(self,other):
        pass

    def __str__(self):
        pass

    def __mul__(self,other):
        sn = self.getNumerator()
        sd = self.getDenominator()
        on = other.getNumerator()
        od = other.getDenominator()
        return Rational(sn*on,sd*od)

    def __add__(self,other):
        sn = self.getNumerator()
        sd = self.getDenominator()
        on = other.getNumerator()
        od = other.getDenominator()
        return Rational(sn*od + on*sd, sd*od)

    def __sub__(self,other):
        pass
    
    def __truediv__(self,other):
        pass
    
    def __repr__(self):
        pass

    
        
