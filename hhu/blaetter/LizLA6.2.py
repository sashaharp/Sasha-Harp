# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:40:45 2018

@author: sashaharp
"""

import numpy as np
 
a = np.arange(1,10)
I = np.array([[1, 0], [0, 1]])

print(a.reshape(3, 3))
print(np.vstack((a, np.zeros(9), np.zeros(9), a)).T)
print(a.reshape(3,3).T.flatten())
print(np.kron(a.reshape(3, 3), I))
print(np.kron(I, a.reshape(3, 3)))
