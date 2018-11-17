import numpy as np
import time
#import pygame
import scipy.misc as smp

 

def rotmatX(deg):
    return np.array([
        [1,0,0,0],
        [0,np.cos(2*np.pi * deg/360), -np.sin(2*np.pi * deg/360), 0],
        [0,np.sin(2*np.pi * deg/360), np.cos(2*np.pi * deg/360), 0],
        [0,0,0,1]
        ])

square = [
    np.array([10, 10, 10, 1]), 
    np.array([-10, 10, 10, 1]), 
    np.array([-10, -10, 10, 1]), 
    np.array([-10, -10, -10, 1]), 
    np.array([10, -10, 10, 1]), 
    np.array([10, -10, -10, 1]), 
    np.array([10, 10, -10, 1]), 
    np.array([-10, 10, -10, 1])]

matrix = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])



for n in range(10):
    data = np.zeros( (400,400,3), dtype=np.uint8 )
    for v in range(0,len(square)):
        square[v] = np.dot(rotmatX(10), v)
        data[square[v][0][0], square[v][0][1]] = [255, 0, 0]

    img = smp.toimage( data )       # Create a PIL image
    img.show()
    time.sleep(5)