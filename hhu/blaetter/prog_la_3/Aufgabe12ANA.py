from math import sqrt

class Quadratic(object):
    def __init__(self, a1, a2, a3):
        self.coeff = [a1, a2, a3]
    def __call__(self, x):
        return self.coeff[0]+self.coeff[0]*x+self.coeff[0]*x**2
    def __add__(self, other):
        if isinstance(other, Quadratic):
            return Quadratic(self.coeff[0] + other.coeff[0], self.coeff[1] + other.coeff[1], self.coeff[2] + other.coeff[2])
        elif isinstance(other, (int, float)):
            return Quadratic(self.coeff[0]+other, self.coeff[1], self.coeff[2])
        else:
            return NotImplemented
    __radd__=__add__
    def __sub__(self, other):
        if isinstance(other, Quadratic):
            return Quadratic(self.coeff[0] - other.coeff[0], self.coeff[1] - other.coeff[1], self.coeff[2] - other.coeff[2])
        elif isinstance(other, (int, float)):
            return Quadratic(self.coeff[0]-other, self.coeff[1], self.coeff[2])
        else:
            return NotImplemented
    def __rsub__(self, other):
        if isinstance(other, Quadratic):
            return Quadratic(-self.coeff[0] + other.coeff[0], -self.coeff[1] + other.coeff[1], -self.coeff[2] + other.coeff[2])
        elif isinstance(other, (int, float)):
            return Quadratic(-self.coeff[0]+other, -self.coeff[1], -self.coeff[2])
        else:
            return NotImplemented
    def root(self): #-p/2+-sqrt(p**2/4-q)
        if(self.coeff[2] == 0):
            if(self.coeff[1] == 0):
                return
            else:
                return -self.coeff[0]/self.coeff[1]
        p = self.coeff[0]/self.coeff[2]
        q = self.coeff[1]/self.coeff[2]
        
        if p**2/4-q == 0:
            return [-p/2]
        elif p**2/4-q > 0:
            return [min(-p/2+sqrt(p**2/4-q), -p/2-sqrt(p**2/4-q)), max(-p/2+sqrt(p**2/4-q), -p/2-sqrt(p**2/4-q))]
        else:
            return []