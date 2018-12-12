#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:41:05 2018

@author: sashaharp
"""
import numpy as np
import matplotlib.pyplot as plt

def plotBildAbb(A):
    x = np.linspace(-1, 1, 150)
    y = np.sqrt(1-x**2)
    cst = np.array([[0,0],[0,1],[1,1],[1,0], [0, 0]])
    ct = np.array(list(zip(x, y)))
    c = np.array([A.dot(co) for co in ct])
    cs = np.array([A.dot(co) for co in cst])
    plt.plot(c[:,0:1].reshape(-1), c[:, 1:].reshape(-1))
    plt.plot(-1*c[:,0:1].reshape(-1), -1*c[:, 1:].reshape(-1))
    plt.plot(cs[:,0:1].reshape(-1), -1*cs[:, 1:].reshape(-1))
    for co,i in [['b',0], ['r',1], ['c',2], ['m',3]]: 
        plt.plot(cs[i:i+1,0:1].reshape(-1), -1*cs[i:i+1, 1:].reshape(-1), co+"o")
    plt.axis('equal', xmin=-1.5, xmax = 1.5, ymin = -1.5, ymax = 1.5)
    plt.show()

plotBildAbb(np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],[np.sin(np.pi/4), np.cos(np.pi/4)]]))