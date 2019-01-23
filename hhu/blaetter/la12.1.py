#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

class Bruch():
    """ Bruchklasse """
    from math import gcd
    
    def __init__(self,zaehler=0, nenner=1):
        if isinstance(nenner, (np.int64, int)):
            if isinstance(zaehler, (np.int64, int)):
                self.zaehler = int(zaehler)
                self.nenner = int(nenner)
            elif isinstance(zaehler, Bruch):
                self.zaehler = zaehler.zaehler
                self.nenner = zaehler.nenner * int(nenner)
            else:
                raise NotImplementedError
        elif isinstance(nenner, Bruch):
            if isinstance(zaehler, (np.int64, int)):
                self.zaehler = int(zaehler) * nenner.nenner
                self.nenner = nenner.zaehler
            elif isinstance(zaehler, Bruch):
                self.zaehler = zaehler.zaehler * nenner.nenner
                self.nenner = zaehler.nenner * nenner.zaehler
            else:
                raise NotImplementedError
        elif nenner == 0:
            raise ZeroDivisionError
        else:
            raise NotImplementedError

        if self.nenner < 0:
            self.zaehler, self.nenner = self.kuerzen(-self.zaehler, -self.nenner)
        else:
            self.zaehler, self.nenner = self.kuerzen(self.zaehler, self.nenner)
            
    # KÃ¼rzen von ZÃ¤hler und Nenner
    def kuerzen(self,zaehler, nenner):
        ggT = self.gcd(zaehler, nenner)
        return zaehler//ggT, nenner//ggT #ganzzahlige Division
    
    def __abs__(self):
        return np.sign(self.zaehler*self.nenner) * self

    # Methode zum Addieren (a+b)
    def __add__(self, other):
        if isinstance(other, (np.int64, int)):
            other = Bruch(other)
        zaehler = self.zaehler*other.nenner + other.zaehler*self.nenner
        nenner = self.nenner*other.nenner
        return Bruch(zaehler, nenner)
    
    # Methode zum Subtrahieren (a-b)
    def __sub__(self, other):
        if isinstance(other, (np.int64, int)):
            other = Bruch(other)
        return self + Bruch(-other.zaehler, other.nenner)
        
    # Methode zum Dividieren (a/b)
    def __truediv__(self, other):
        if isinstance(other, (np.int64, int)):
            other = Bruch(other)
        zaehler = self.zaehler * other.nenner
        nenner = self.nenner * other.zaehler
        return Bruch(zaehler, nenner)
    
    # Methode zum Multiplizieren (a*b)
    def __mul__(self, other):
        if isinstance(other, (np.int64, int)) or (isinstance(other, float) and other == int(other)):
            other = Bruch(int(other))
        #print(other)
        zaehler = self.zaehler * other.zaehler
        nenner = self.nenner * other.nenner
        return Bruch(zaehler, nenner)

     # Umgekehrte Multiplikation, so dass auch Skalar*Bruch funktioniert:        
    __rmul__ = __mul__
    
    # Umgekehrte Addition, so dass auch Skalar+Bruch funktioniert:        
    __radd__ = __add__
    
    # Umgekehrte Subtraktion, so dass auch Skalar-Bruch funktioniert:
    def __rsub__(self, other):
        if isinstance(other, (np.int64, int)):
            other = Bruch(other)
        return other - self
    
    # Umgekehrte Division, so dass auch Skalar/Bruch funktioniert:
    def __rtruediv__(self, other):
        if isinstance(other, (np.int64, int)):
            other = Bruch(other)
        return other / self
    
    #==
    def __eq__(self, other):
        if isinstance(other, (int, np.int64, float)):
            return float(self) == other
        else:
            return float(self) == float(other)
    
    #<
    def __lt__(self, other):
        if isinstance(other, (int, np.int64, float)):
            return float(self) < other
        else:
            return float(self) < float(other)
    
    #>
    def __gt__(self, other):
        if isinstance(other, (int, np.int64, float)):
            return float(self) > other
        else:
            return float(self) > float(other)
    
    #<=
    def __le__(self, other):
        if isinstance(other, (int, np.int64, float)):
            return float(self) <= other
        else:
            return float(self) <= float(other)
    
    #>=
    def __ge__(self, other):
        if isinstance(other, (int, np.int64, float)):
            return float(self) >= other
        else:
            return float(self) >= float(other)
    #!=
    def __ne__(self, other):
        if isinstance(other, (int, np.int64, float)):
            return float(self) != other
        else:
            return float(self) != float(other)

    __rlt__ = __gt__
    __rgt__ = __lt__
    __rle__ = __ge__
    __rge__ = __le__
    __req__ = __eq__
    __rne__ = __ne__
    #+=
    def __iadd__(self, other):
        return self + other
    #-=
    def __isub__(self, other):
        return self - other
    #*=
    def __imul__(self, other):
        return self * other
    #/=
    def __idiv__(self, other):
        return self / other
    
    # Methode zum Potenzieren, damit Bruch**Integer funktioniert
    def __pow__(self, skalar):
        if isinstance(skalar, int) and skalar >= 0:
            return Bruch(self.zaehler**skalar, self.nenner**skalar)
        elif isinstance(skalar, int) and skalar < 0:
            return Bruch(self.nenner**(-skalar), self.zaehler**(-skalar))
        else:
            raise NotImplementedError
    
    # In float umwandeln
    def __float__(self):
        return self.zaehler/self.nenner
    
    # Zur ReprÃ¤sentation (beim Eintippen in die Konsole, oder print())
    def __str__(self):
        return '{:d}/{:d}'.format(self.zaehler,self.nenner) 
    
    def __repr__(self):
        return '{:d}/{:d}'.format(self.zaehler,self.nenner) 


def LR_kompakt(A):
    A = A.astype(Bruch).copy()
    n = A.shape[0]
    p = np.arange(n)
    for kk in range(n-1):
        # Pivotelement ist das erste nicht-null Element der Spalte:
        #ll = kk + np.flatnonzero(A[kk:, kk])[0]
        # Alternative: Pivotelement ist das betragsgrÃ¶ÃŸte Element der Spalte:
        ll = kk + np.argmax(abs(A[kk:, kk]))
        A[[ kk, ll ]] = A[[ ll, kk ]]
        p[[ kk, ll ]] = p[[ ll, kk ]]
        A[kk+1:, kk] /= Bruch(A[kk, kk])
        if(A[kk+1, kk] is Bruch):
                z, n = A[kk+1, kk].kuerzen(A[kk+1, kk].zaehler, A[kk+1, kk].nenner)
                A[kk+1, kk] = Bruch(z, n)
        if(A[kk, kk+1] is Bruch):
                z, n = A[kk, kk+1].kuerzen(A[kk, kk+1].zaehler, A[kk, kk+1].nenner)
                A[kk, kk+1] = Bruch(z, n)
        A[kk+1:, kk+1:] -= np.dot(A[kk+1:, [kk]], A[[kk] , kk+1:])
        if(A[kk+1, kk+1] is Bruch):
                z, n = A[kk+1, kk+1].kuerzen(A[kk+1, kk+1].zaehler, A[kk+1, kk+1].nenner)
                A[kk+1, kk+1] = Bruch(z, n)
        # Achtung:  A[kk+1:, kk] liefert einen eindimensionalen Array,
        #           A[kk+1:, [kk]] einen zweidimensionalen 
    return p, A



def TestLR_Bruch(testfunktion):
    m = 10
    print('Ihre Funktion wird jetzt mit 3 ({0}x{0})-Matrizen getestet'.format(m));
    A = _zufallsmatINT(m)
    B = _zufallsmatBRUCH(m)
    C1 = _zufallsmatINT(m)
    C = _zufallsmatBRUCH(m)
    for i in range(m):
        for j in range(m):
            zufallsindex = np.random.randint(0,2)
            if zufallsindex == 0:
                C[i, j] = C1[i, j]
    texte = ['Matrix mit Integer-EintrÃ¤gen',\
             'Matrix mit Bruch-EintrÃ¤gen',\
             'Matrix mit gemischten EintrÃ¤gen']
    
    tb = 0
    for M, text in zip([A, B, C], texte):
        print('Teste ' + text + ':')
        p, MLR = testfunktion(M)
        R = np.triu(MLR)
        L = np.eye(MLR.shape[0], dtype=int) + np.tril(MLR, -1)
        erg = np.equal(M[p,:],np.dot(L,R)).all()
        print("Das Ergebnis ist {0}.".format(erg));
        if erg:
            tb += 1;
    
    print('{0} von {1} Tests erfolgreich'.format(tb, 3));

def _zufallsmatINT(m, Null = True):
    mat = np.random.randint(-20,20, m**2)
    if Null == False:
        mat[mat == 0] += 1
    return mat.reshape(m,m)

def _zufallsmatBRUCH(m):
    ZufINT1 = _zufallsmatINT(m)
    ZufINT2 = _zufallsmatINT(m, Null = False)
    MatBRUCH = np.zeros((m,m), dtype=Bruch)
    for i in range(m):
        for j in range(m):
            MatBRUCH[i,j] = Bruch(int(ZufINT1[i,j]), int(ZufINT2[i,j]))
    return MatBRUCH


def QbTest(testfunktion):
    m, n = 20, 15
    print('Ihre Funktion wird jetzt mit einer ({0}x{0})- '.format(m)\
          +'und einer ({0}x{1})-Matrix getestet'.format(m, n));
    t = 0
    for mm, nn in zip([m, m], [m, n]):   
        Vtest = np.tril(np.random.rand(mm, nn))
        Vtest = Vtest/np.linalg.norm(Vtest, axis=0)
        btest = np.random.rand(mm,1)
        Qb1 = testfunktion(Vtest, btest)
        Qb2 = _Qblang(Vtest, btest)
        if np.allclose(Qb1, Qb2):
            t += 1
    print('{0} von {1} Tests erfolgreich'.format(t, 2));
    
def _Qblang(V, b):
    m, n = V.shape
    Q = np.eye(m)
    for k in range(n):
        v = V[k:, [k]]
        Qk = np.eye(m)
        Qk[k:, k:] = np.eye(m-k) - 2*(v @ v.T)
        Q = Q @ Qk
    return Q@b

TestLR_Bruch(LR_kompakt)