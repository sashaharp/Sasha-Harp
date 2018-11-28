# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 21:38:03 2018

@author: sashaharp
"""
import matplotlib.pyplot as plt
import numpy as np
class Polynom():
    
    def __init__(self,dp):
        # falls die Funktion konstant ist
        if isinstance(dp,(int,float,complex)):
            dp = {0:dp}
        self.dp = dp
        self.degree = max(dp.keys())
        assert all(isinstance(x, int) and x >= 0 for x in dp.keys()),\
            "Die Exponeten (keys) müssen natürliche Zahlen (einschl. 0) sein."
        
    def __repr__(self):
        polystr = ''
        for k in sorted(self.dp):
            polystr = polystr + '{0:+g}*X^{1}'.format(self.dp[k],k)
        polystr = polystr.replace('X^0', '1')
        polystr = polystr.replace('1*', '')
        polystr = polystr.replace('*1', '')
        polystr = polystr.replace('X^1', 'X')
        if polystr[0] == '+':
            polystr = polystr[1:]
        return 'Polynom: ' + polystr 
    
    def __add__(self,other):
        # Die Addition ist im Skript etwas umständlicher, weil der copy-
        # Befehl noch nicht vorgekommen ist. 
        erg = self.dp.copy()
        for k in other.dp:
            if k in self.dp:
                erg[k] += other.dp[k]
            else:
                erg[k] = other.dp[k]
        return Polynom(erg)
    
    def __sub__(self,other):
        # s.o.
        erg = self.dp.copy()
        for k in other.dp:
            if k in self.dp:
                erg[k] -= other.dp[k]
            else:
                erg[k] = -other.dp[k]
        return Polynom(erg)
    
    # Zum Auswerten der Funktion:
    def __call__(self,x):
        return sum([self.dp[k]*x**k for k in self.dp])
    
    # Multiplikation mit Skalaren und Polynomen:
    def __mul__(self,other):
        erg = dict()
        if isinstance(other,(int,float,complex)):
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
   
    # Umgekehrte Multiplikation, so dass auch Skalar*Polynom funktioniert:        
    __rmul__ = __mul__
    
    def diff(self):
        erg = dict()
        if self.degree == 0:
            erg[0] = 0
        else:
            for i in self.dp:
                if i != 0:
                    erg[i-1] = self.dp[i]*i
        return Polynom(erg)
    
    def integrate(self):
        erg = dict()
        for i in self.dp:
            erg[i+1] = self.dp[i]/(i+1)
        return Polynom(erg)
    
    def integral(self, a, b):
        intPol = self.integrate()
        return intPol(b) - intPol(a)
    def plot(self, fignum = None, xmin = 0, xmax = 1, num = 50, style = "ks:"):
        x = np.linspace(xmin, xmax, num)
        y = np.array([sum([(xn ** a) * b for a,b in self.dp.items()]) for xn in x]) #items gibt paare vom 1. und 2. dict dp
        plt.plot(x,y, style, label = self.__repr__())
        plt.legend()

# Test der Klasse Polynom
p = Polynom({0:3,1:1,2:8,4:5})
p.plot()
print('Polynom p:', p)
print('Erste Ableitung:', p.diff())
print('Stammfunktion:', p.integrate())
print('Integralwert von p über [0,1]:', p.integral(0,1))