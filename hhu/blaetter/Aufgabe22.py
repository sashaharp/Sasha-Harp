#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:07:43 2018

@author: sashaharp
"""

import numpy as np

a = np.arange(1, 10)
I = np.array([[1, 0],[0, 1]])

a = a.reshape(3, 3)
print(a)
print(np.vstack((a.reshape(1, 9), np.zeros(9).reshape(1, 9), np.zeros(9).reshape(1, 9), a.reshape(1, 9))).T)
print(a.flatten())
print(np.kron(a, I))
print(np.kron(I, a))