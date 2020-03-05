import numpy as np
import matplotlib.pylab as plt
import sys

def Bezier(points, num):
    res = []
    ts = np.linspace(0, 1, num)
    for t in ts:
        res.append(points[0]*(1-t)**3 + points[1]*3*t*(1-t)**2 + points[2]*3*(1-t)*t**2 + points[3]*t**3)
    return np.array(res)
def reOrder(points, bezier):
    p = points.tolist()
    rp = []
    cp = []
    for b in bezier:
        s = -1.0
        for pp in p:
            if s < 0 or np.linalg.norm(b-pp) < s:
                s = np.linalg.norm(b-pp)
                cp = pp
        rp.append(list(cp))
        p.remove(cp)
    return np.array(rp)
def Error(p1, p2):
    sum = 0
    for x in range(min(len(p1), len(p2))):
        sum += np.linalg.norm(p1[x]-p2[x])**2
    return sum

points = []
p = sys.argv[1].split(';')
for n in p:
    points.append(n.split(','))
sample = np.array(points).astype(int)

start = sample[0]
end = sample[len(sample)-1]
BP = np.array([start, [start[0]+(end[0]-start[0])/3.0, start[1]+(end[1]-start[1])/3.0], [start[0]+2*(end[0]-start[0])/3.0, start[1]+2*(end[1]-start[1])/3.0], end]) #start point and end point would be given by algo

sample = reOrder(sample, Bezier(BP, len(sample)))
adjust = np.array([[[0, 0], [x%3-1, (x//3)%3-1], [(x//9)%3-1, (x//27)%3-1], [0, 0]] for x in range(81)])
doNext = True
n = 0
while doNext and n < 1000:
    maxDiff = []
    currB = Bezier(BP, len(sample))
    err = Error(currB, sample)
    for a in adjust:
        newBP = BP + a
        newB = Bezier(newBP, len(sample))
        newErr = Error(newB, sample)
        #print(newErr)
        if err - newErr > 0.1:
            err = newErr
            maxDiff = a
    if len(maxDiff) != 0:
        BP = BP + maxDiff
    else:
        doNext = False
    n = n + 1
BP = np.around(BP).astype(int)
print("CB" + BP[0][0].__str__()+"," + BP[0][1].__str__()+" " + BP[1][0].__str__()+"," + BP[1][1].__str__()+" " + BP[2][0].__str__()+"," + BP[2][1].__str__()+" " + BP[3][0].__str__()+"," + BP[3][1].__str__() + "CB")

