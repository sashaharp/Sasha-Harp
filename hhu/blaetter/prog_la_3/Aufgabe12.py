#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polynom(object):
    """ Polynomklasse Beschreibung .....
    """
    def __init__(self,dp):
        if isinstance(dp,(int,float,complex)):
            dp = {0:dp}
        self.dp = dp
        self.degree = max(dp.keys())
        
    def __repr__(self):
        polystr = ''
        for k in sorted(self.dp):
            polystr = polystr + '{0:+g}*X^{1}'.format(self.dp[k],k)
        return 'Polynom: ' + polystr 
    
    def __add__(self,other):
        spow = set(self.dp.keys())
        opow = set(other.dp.keys())
        pows = spow.union(opow)
        pps = dict()
        for k in pows:
            if k in spow:
                if k in opow:
                    pps[k] = self.dp[k] + other.dp[k]
                else:
                    pps[k] = self.dp[k]
            else:
                pps[k] =  other.dp[k]    
        return Polynom(pps)
    
    def __sub__(self,other):
        """ Substraktion zweier Polynomen 
        """
        spow = set(self.dp.keys())
        opow = set(other.dp.keys())
        pows = spow.union(opow)
        erg = dict()
        for k in pows:
            if k in spow:
                if k in opow:
                    erg[k] = self.dp[k] - other.dp[k]
                else:
                    erg[k] = self.dp[k]
            else:
                erg[k] = -other.dp[k]    
        return Polynom(erg)
    
    def __call__(self,x):
        """ Auswertung des Polynoms 
        """
        return sum([self.dp[k]*x**k for k in self.dp])
    
    def __mul__(self, other):
        tempdict = {0:0}
        if isinstance(other,(int,float,complex)):
            for k in self.dp:
                tempdict[k] = self.dp[k] * other       
            return Polynom(tempdict)
        elif isinstance(other, Polynom):
            for i in self.dp.keys():
                for j in other.dp.keys():
                    if (i+j in tempdict.keys()):
                        tempdict[i+j] += self.dp[i]*other.dp[j]
                    else:
                        print(j+i)
                        tempdict[i+j] = self.dp[i]*other.dp[j]
            return Polynom(tempdict)
        else:
            return NotImplemented
            
    __rmul__ = __mul__

    def diff(self):
        tempdict = {}
        for i in self.dp.keys():
            if i > 0:
                tempdict[i-1] = i*self.dp[i]
        return Polynom(tempdict)

    def integral(self, a, b):
        tempdict = {}
        for i in self.dp.keys():
            tempdict[i+1] = self.dp[i]/(i+1)
        tempPoly = Polynom(tempdict)
        return tempPoly(b) - tempPoly(a)
            

pd = {0:3,1:1,2:8,4:5}
p = Polynom(pd)

print("Ableitung von " + str(p) + " ist " + str(p.diff()))

print("und das Integral ist " + str(p.integral(0, 1)))