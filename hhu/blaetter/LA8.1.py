#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:48:43 2018

@author: mfischer
"""

# sphere.py fÃ¼r Blatt 8, Aufgabe 29

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotSphere():
    phi1D = np.linspace(np.pi/4, 3*np.pi/4, 10)[1:-1]
    theta1D = np.linspace(-3*np.pi/4, 3*np.pi/4, 22)[:-1]
    phi, theta = np.meshgrid(phi1D,theta1D)

    x0 = (np.sin(phi)*np.cos(theta)).flatten()
    x1 = (np.sin(phi)*np.sin(theta)).flatten()
    x2 = np.cos(phi).flatten()

    xYin = np.vstack([ x0, x1, x2])
    xYang = np.vstack([-x0, x2, x1])
    x = np.hstack((xYin, xYang))

    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111, projection='3d')

    m1 = np.min(x)
    m2 = np.max(x)
    ax.set_xlim3d(m1, m2)
    ax.set_xlabel('$x_0$')
    ax.set_ylim3d(m1, m2)
    ax.set_ylabel('$x_1$')
    ax.set_zlim3d(m1, m2)
    ax.set_zlabel('$x_2$')    
        
    for k in range(x.shape[1]):
        col = plt.cm.inferno(k/x.shape[1]) #https://matplotlib.org/gallery/color/colormap_reference.html
        ax.quiver3D(0, 0, 0, x[0,k], x[1,k], x[2,k], colors = col)

    plt.show()

def plotBildSphere(A):
    
    u = np.array([1, 2, 3]).reshape(3, 1)

    phi1D = np.linspace(np.pi/4, 3*np.pi/4, 10)[1:-1]
    theta1D = np.linspace(-3*np.pi/4, 3*np.pi/4, 22)[:-1]
    phi, theta = np.meshgrid(phi1D,theta1D)

    x0 = (np.sin(phi)*np.cos(theta)).flatten()
    x1 = (np.sin(phi)*np.sin(theta)).flatten()
    x2 = np.cos(phi).flatten()

    xYin = np.vstack([ x0, x1, x2])
    xYang = np.vstack([-x0, x2, x1])
    x = np.hstack((xYin, xYang))

    fig = plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(122, projection='3d')
    ax2 = fig.add_subplot(121, projection='3d')

    ax1.set_xlabel('$x_0$')
    ax1.set_ylabel('$x_1$')
    ax1.set_zlabel('$x_2$')    
        
    for k in range(x.shape[1]):
        col = plt.cm.inferno(k/x.shape[1]) #https://matplotlib.org/gallery/color/colormap_reference.html
        ax1.quiver3D(0, 0, 0, x[0,k], x[1,k], x[2,k], colors = col)
    ax1.quiver3D(0, 0, 0, u[0, 0], u[1, 0], u[2, 0], colors = plt.cm.hot(0))
    
    m1 = np.min(x)
    m2 = np.max(x)
    x = A@x
    u = A@u #do you mean that?
    m1 = min(np.min(x), m1)
    m2 = max(np.max(x), m1)
    ax2.set_xlim3d(m1, m2)
    ax1.set_xlim3d(m1, m2)
    ax2.set_xlabel('$x_0$')
    ax2.set_ylim3d(m1, m2)
    ax1.set_ylim3d(m1, m2)
    ax2.set_ylabel('$x_1$')
    ax2.set_zlim3d(m1, m2)
    ax1.set_zlim3d(m1, m2)
    ax2.set_zlabel('$x_2$')  

    for k in range(x.shape[1]):
        col = plt.cm.inferno(k/x.shape[1]) #https://matplotlib.org/gallery/color/colormap_reference.html
        ax2.quiver3D(0, 0, 0, x[0,k], x[1,k], x[2,k], colors = col)
    ax2.quiver3D(0, 0, 0, u[0, 0], u[1, 0], u[2, 0], colors = plt.cm.hot(0))

    plt.show()

plotBildSphere(np.array([2, 0, 0, 0, 3, 0, 0, 0, -1]).reshape(3, 3))
plotBildSphere(np.array([[3, 1, 0],[1, 2, 0],[0, 0, 1]]))
u = (1/np.sqrt(14))*np.array([1, 2, 3]).reshape(1, 3)
plotBildSphere(np.identity(3)-u@u.transpose())