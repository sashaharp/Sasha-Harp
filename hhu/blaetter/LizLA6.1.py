# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:32:58 2018

@author: sashaharp
"""

import numpy as np

A = np.array([[2, -1, 0],[-1, 2, -1], [0, 1, -2]])
B = np.array([[1, 3, 5], [5,4,3], [3,5,1]])

x = np.ones(3).reshape(3, 1)
y = np.arange(1, 4).reshape(1, 3)
z = np.arange(-1, 2)

A @ B
A * B#<--bs
A * y#<--bs
y * A#<--bs
A @ x
#A @ y
#x @ A
y @ A
B @ z
z @ B
B * z#<--bs
z * B#<--bs
print(x * y)
y * x
y @ x
x @ y
x * z
y * z
z * x
#z @ y
y @ z