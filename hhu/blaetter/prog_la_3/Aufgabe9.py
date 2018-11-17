#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ggt_it(a, b):
    while b != 0:
        h = a%b
        a = b
        b = h
    return a

def ggt_it_zusatz(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def ggt_rek(a, b):
    if b == 0:
        return a
    return ggt_rek(b, a%b)



print("ggt_it von 2469134 und 8641969 ist: " + str(ggt_it(2469134, 8641969)))
print("ggt_it_zusatz von -345 und 15 ist: " + str(ggt_it_zusatz(345, 15)))
print("ggt_rek von 7892389 und -3 ist: " + str(ggt_rek(7892389, -3)))