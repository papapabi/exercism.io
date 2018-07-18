from math import gcd

class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("denom cannot be 0")
        _gcd = gcd(numer, denom)
        self.numer = numer / _gcd
        self.denom = denom / _gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}r'.format(self.numer, self.denom)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
