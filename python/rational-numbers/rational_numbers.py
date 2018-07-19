from math import gcd


def _simplest_form(numer, denom):
    """Returns the simplest form of a numer and denom, in a 2-tuple"""
    _gcd = gcd(numer, denom)
    if numer * denom > 0:
        numer = abs(numer)
        denom = abs(denom)
    else:
        numer = -abs(numer)
        denom = abs(denom)
    return (numer // _gcd, denom // _gcd)


class Rational(object):

    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("denom cannot be 0")
        self.numer, self.denom  = _simplest_form(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}r'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer, denom)

    def __abs__(self):
        abs_numer = abs(self.numer)
        abs_denom = abs(self.denom)
        return Rational(abs_numer, abs_denom)

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
