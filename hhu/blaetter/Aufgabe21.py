#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:58:48 2018

@author: sashaharp
"""
import numpy as np

A = np.array([[2, -1, 0],[-1, 2, -1],[0, 1, -2]])
B = np.array([[1, 3, 5],[5, 4, 3],[3, 5, 1]])
x = np.ones(3).reshape(3, 1)
y = np.array([[1, 2, 3]])
z = np.array([-1, 0, 1])
print(y.shape)
print(z.shape)
A @ B
A * B
A * y
y * A
A @ x
#A @ y
#x @ A
y @ A
B @ z
z @ B
B * z
z * B
x * y
y * x
y @ x
x @ y
x * z
y * z
z * x
#z @ y
y @ z