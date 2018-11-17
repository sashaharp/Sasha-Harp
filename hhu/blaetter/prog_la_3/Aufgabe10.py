#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Bruch(object):
    
    # Initialisieren
    def __init__(self, __zaehler, __nenner):
        z = __zaehler
        n = __nenner
        if n == 0:
            print("division by zero\nsetting the fraction to 0/0")
            self.__zaehler = 0
            self.__nenner = 0
            return
        self.kuerzen(z, n)
    
    @property
    def zaehler(self):
        return self.__zaehler

    @property
    def nenner(self):
        return self.__nenner

    @zaehler.setter
    def zaehler(self, x):
        self.__zaehler
        self.kuerzen

    @nenner.setter
    def nenner(self, x):
        if x != 0:
            self.__nenner = x
            self.kuerzen
        else:
            print("division by zero\nsetting the fraction to 0/0")
            self.__zaehler = 0
            self.__nenner = 0

    # Kürzen von Zähler und Nenner
    def kuerzen(self, __zaehler, __nenner):
        z = __zaehler
        n = __nenner
        a = self.ggt(__zaehler, __nenner)
        while a != 1:
            z /= a
            n /= a
            a = self.ggt(z, n)
        self.__zaehler = int(z)
        self.__nenner = int(n)
        return z, n
        
    def ggt(self, a, b):
        while b != 0:
            a, b = b, a%b
        return a
    
    # Methode zum Addieren (a+b)
    def __add__(self, other):
        if isinstance(other, Bruch):
            if(other.nenner == 0 or self.__nenner == 0):
                return Bruch(0, 0)
            kgv = abs(self.__nenner*other.nenner) / self.ggt(self.__nenner, other.nenner)
            b = Bruch(self.__zaehler*kgv/self.__nenner + other.zaehler*kgv/other.nenner, kgv)
            b.kuerzen
        elif isinstance(other, int):
            b = Bruch(self.__zaehler + other*self.__nenner, self.__nenner)
        else:
            return NotImplemented
        return b

    def __radd__(self, other):
        return self.__add__(other)
    
    # Methode zum Subtrahieren (a-b)
    def __sub__(self, other):
        if(other.nenner == 0 or self.__nenner == 0):
            return Bruch(0, 0)
        return self.__add__(other*-1)

    def __rsub__(self, other):
        if(self.__nenner == 0):
            return Bruch(0, 0)
        return self.__add__(other*-1) * -1

    # Methode zum Dividieren (a/b)
    def __truediv__(self, other):
        if isinstance(other, Bruch):
            if(other.nenner == 0 or self.__nenner == 0):
                return Bruch(0, 0)
            return self.__mul__(Bruch(other.nenner, other.zaehler))
        elif isinstance(other, int):
            return self.__mul__(Bruch(1, other))
        else:
            return NotImplemented
    
    # Methode zum Dividieren (a/b)
    def __rtruediv__(self, other):
        if isinstance(other, int):
            return self.__mul__(Bruch(1, other))
        else:
            return NotImplemented
    
    # Methode zum Multiplizieren (a*b)
    def __mul__(self, other):
        if isinstance(other, Bruch):
            b = Bruch(self.__zaehler*other.zaehler, self.__nenner*other.nenner)
            b.kuerzen
        elif isinstance(other, int):
            b = Bruch(self.__zaehler*other, self.__nenner)
        else:
            return NotImplemented
        return b
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    # In float umwandeln
    def tofloat(self):
        if self.__nenner == 0:
            return "NaN"
        return self.zaehler/self.nenner
    
    ''' Diese beiden Methoden dienen dazu, dass Sie den Bruch sehen wenn die
    ein Bruch-Objekt in die Konsole tippen oder print() übergeben.
    Bei 0/0 wird "NaN" zurückgegeben, um zu verdeutlichen, dass das nicht
    korrekt ist.
    Wenn die Attribute für Zähler und Nenner bei Ihnen "__zaehler" und "__nenner"
    heißen, müssen Sie hier nichts ändern.
    '''
    def __str__(self):
        return '{:d}/{:d}'.format(self.__zaehler,self.__nenner) if self.__nenner>0 else 'NaN'
    
    def __repr__(self):
        return '{:d}/{:d}'.format(self.__zaehler,self.__nenner) if self.__nenner>0 else 'NaN'

#tests
for a in range(-20, 20):
    for b in range(-20, 20):
        for c in range(-20, 20):
           for d in range(-20, 20):
               ba = Bruch(a, b)
               bb = Bruch(c, d)
               print(ba)
               print(bb)
               print("+: " + str(ba+bb))
               print("-: " + str(ba-bb))
               print("*: " + str(ba*bb))
               print("/: " + str(ba/bb))
