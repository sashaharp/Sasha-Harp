import numpy as numpy
import matplotlib.pyplot as plt
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stand: Montag 07.01.19

"""

# In diesem Modul finden Sie die aktuelle MusterlÃ¶sung zur Polynomklasse und zu
# verschiedenen Aufgaben, die mit dieser Klasse zusammenhÃ¤ngen, u.a.:
# MusterlÃ¶sung von Blatt 8, Aufgabe 31

# Sie kÃ¶nnen die Datei als Skript ausfÃ¼hren, oder als Modul z.B. mit
# import polynompy as pp 
# laden.

# Neue ErgÃ¤nzungen/Erweiterungen in der Klasse Polynom, die weder im Skript 
# stehen, noch explizit in einer Aufgabe gefordert wurden:
# - __add__ und __sub__ gekÃ¼rzt
# - skalare Addition und Subtraktion ergÃ¤nzt (siehe __add__, __sub__, __radd__, __rsub__)
# - skalare Division ergÃ¤nzt (siehe __truediv__)
# - Plot-Routine erweitert, sodass nun eine Figure und ein Axen-Objekt ausgegeben werden 
# - __repr__ stellt nun das Polynom mit gekÃ¼rtzten Koeffizienten dar

class Polynom():
    """ Polynomklasse """
    # Hier ist es sinnvoll, die benÃ¶tigten Pakete direkt in die Klasse zu laden.
    # So ist sichergestellt, dass die Klasse die notwendigen
    # Pakete immer kennt.
    # Methoden aus diesen Pakten mÃ¼ssen dann mit einem "self" davor geladen werden.
    import numpy as np
    import matplotlib.pyplot as plt
    
    def __init__(self, dp):
        # falls die Funktion konstant ist
        if isinstance(dp, (int, float, complex)):
            dp = {0:dp}
        self.dp = dp
        self.degree = max(dp.keys())
        assert all(isinstance(x, int) and x >= 0 for x in dp.keys()),\
            "Die Exponenten (keys) mÃ¼ssen natÃ¼rliche Zahlen (einschl. 0) sein."
        
    def __repr__(self):
        polystr = ''
        for k in sorted(self.dp):
            polystr = polystr + '+{0:.2f}*X^{1}'.format(self.dp[k], k)
        polystr = polystr.replace('X^0', '1')
        polystr = polystr.replace('+-', '-')
        polystr = polystr.replace('1*', '')
        polystr = polystr.replace('*1', '')
        polystr = polystr.replace('X^1', 'X')
        if polystr[0] == '+':
            polystr = polystr[1:]
        return 'Polynom: ' + polystr 
    
    def __add__(self, other):
        # Skalare Addition
        if isinstance(other, (int, float, complex)):
            other = Polynom(other)
        # eine MÃ¶glichkeit zur Addition:
        # hier ist eine noch kÃ¼rzere Variante: .get(n,0) greift auf den Eintrag n 
        # des Dictionaries und gibt falls der nicht vorhanden ist
        # das zweite Argument (hier 0) zurÃ¼ck
        erg = dict((n, self.dp.get(n, 0) + other.dp.get(n, 0)) for n in set(self.dp).union(set(other.dp)))
        return Polynom(erg)
    
    def __sub__(self, other):
        # s.o.
        if isinstance(other, (int, float, complex)):
            other = Polynom(other)
        erg = dict((n, self.dp.get(n, 0)-other.dp.get(n, 0)) for n in set(self.dp).union(set(other.dp)))
        return Polynom(erg)
    
    def __rsub__(self, other):
        # damit auch fÃ¼r ein Skalar a und ein Polynom p auch a-p funktioniert
        if isinstance(other, (int, float, complex)):
            other = Polynom(other)
        return other - self

    # Zum Auswerten der Funktion (normale Auswertung und Auswertung mit Horner ist mÃ¶glich):
    def __call__(self, x, method=None):
        if method == None:
            return sum([self.dp[k]*x**k for k in self.dp])
        elif method == 'Horner':
            return self.__Horner__(x)
        
    # Multiplikation mit Skalaren und Polynomen:
    def __mul__(self, other):
        erg = dict()
        if isinstance(other, (int, float, complex)):
            for k in self.dp:
                erg[k] = self.dp[k] * other
        else:
            for i in self.dp:
                for j in other.dp:
                    if i+j in erg:
                        erg[i+j] += self.dp[i]*other.dp[j]
                    else:
                        erg[i+j] = self.dp[i]*other.dp[j]
        return Polynom(erg)
    
    def __truediv__(self, other):
        # Wir wollen fÃ¼r ein Polynom p und ein Skalar a p/2 fuer 1/2 * p schreiben kÃ¶nnen
        if isinstance(other, (int, float, complex)):
            erg = dict((n, self.dp[n]/other) for n in self.dp)
        else:
            raise NotImplementedError("Polynomdivision nicht implementiert")   
        return Polynom(erg)
    
    # Umgekehrte Multiplikation, so dass auch Skalar*Polynom funktioniert:        
    __rmul__ = __mul__
    # Umgekehrte Addition, so dass auch Skalar+Polynom funktioniert:        
    __radd__ = __add__
    
    def conjugate(self):
        """ Komplexe Konjugation der Koeffizienten """
        erg = self.dp.copy()
        for i in self.dp:
            if isinstance(self.dp[i], complex):
                erg[i] = self.dp[i].conjugate()
        return Polynom(erg)
    
    def diff(self):
        """ Ableitung des Polynoms """
        erg = dict()
        if self.degree == 0:
            erg[0] = 0
        else:
            for i in self.dp:
                if i != 0:
                    erg[i-1] = self.dp[i]*i
        return Polynom(erg)
    
    def integrate(self):
        """ Stammfunktion des Polynoms """
        erg = dict()
        for i in self.dp:
            erg[i+1] = self.dp[i]/(i+1)
        return Polynom(erg)
    
    def integral(self, a, b):
        """ Berechent Integral von a bis b """ 
        intPol = self.integrate()
        return intPol(b) - intPol(a)
    
    def plot(self, fig=None, ax=None, xmin=0, xmax=1, num=50, style='k--s',\
             method=None):
        """ Plotroutine fÃ¼r Klasse Polynom
        
         fig -- Figurehandle von pyplot.figure() \n
         ax -- Koordinatensysterm \n
         [xmin,xmax]  -- Intervall Ã¼ber dem gezeichnet werden soll \n
         num -- Anzahl der Punkte \n
         style -- Linienstil
        """
        if fig == None:
            fig = self.plt.figure()
            
        if ax == None:
            ax = fig.add_subplot(111)
        x = self.np.linspace(xmin, xmax, num)
        if method is None:
            ax.plot(x, self(x), style, label='${}$'.format(self))
        elif method == 'Horner':
            ax.plot(x, self.__Horner__(x), style, label='${}$'.format(self))
        else:
            raise NotImplementedError("Verfahren zur Auswertung nicht implementiert")
        ax.legend()
        return fig, ax
    
    def __Horner__(self, x):
        """ Auswertung mit dem Horner-Schema (Aufg. 33) """
        # Die Funktion ist "versteckt", d.h. p.Horner(x) ist nicht bekannt,
        # dafÃ¼r aber p.__Horner__(x)
        erg = 0
        mk = self.degree
        for k in sorted(self.dp, reverse=True):
            erg = self.dp[k] + erg*x**(mk - k)
            mk = k
        return erg

# MusterlÃ¶sung von Aufgabe 31 (unter Verwendung der Polynom-Klasse)
def Legendre(n, method=None):
    """ Legendre Polynom vom Grad n """
    assert n >= 0 and isinstance(n, int), \
        "n ist keine natÃ¼rliche Zahl."
        
    if method == None: #iterative Version
        if n == 0: 
            return Polynom(1)
    
        P_nm1 = Polynom(1)
        P_n = Polynom({1:1})
        x = Polynom({1:1})
        for k in range(2, n+1):
            P_n, P_nm1 = ((2*k-1)*x*P_n - (k-1)*P_nm1) / k, P_n
        return P_n
    
    elif method == 'Rec': #rekursive Version
        if n == 0: 
            return Polynom(1)
        elif n == 1:
            return Polynom({1:1})
        else:
            x = Polynom({1:1})
        return ((2*n-1)*x*Legendre(n-1, method='Rec') - (n-1)*Legendre(n-2, method='Rec')) / n

def Monombasis(n):
    """Berechnet die Monombasis [1,x,...,x**n]"""
    return [Polynom({k:1}) for k in range(n+1)] 
    
def SProdKoeff(p, q):
    from numpy import sqrt
    q = q.conjugate()
    return sqrt(sum([p.dp.get(n, 0)*q.conjugate().dp.get(n, 0) for n in set(p.dp).union(set(q.dp))]))

def lagrange(*c):
    l = []
    for i in range(len(c)):
        temp = Polynom(1)
        for j in range(len(c)):
            if(i!=j):
                temp *= Polynom({1: 1/(c[i]-c[j]), 0: c[i]/(c[i]-c[j])})
        l.append(temp)
    return l

def getC(n):
    return [numpy.cos((2*j+1)*numpy.pi/(2*(n+1))) for j in range(n+1)]

c=getC(6)
ls = lagrange(c[0], c[1], c[2], c[3], c[4], c[5], c[6])

fig = plt.figure()
ax = fig.add_subplot(111)

for l in ls:
    l.plot(fig, ax, -1, 1, 100, "")

plt.show()