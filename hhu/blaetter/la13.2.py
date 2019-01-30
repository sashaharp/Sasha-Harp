import locale
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.widgets import Slider, Button

#for thousand separators:
locale.setlocale(locale.LC_NUMERIC, "en_US.UTF-8")

tqs = []

#loop through file
with open("Planet.dat") as file:
    for l in file.readlines():
        tqs.append([locale.atof(l.split(" ")[i]) for i in range(4)])

tqs = np.array(tqs)

#algo
A = np.vstack([np.sin(tqs[:,0]), np.cos(tqs[:,0]), np.ones(len(tqs[:,0]))]).T

x = la.solve(A.T@A, A.T@tqs[:,1:])

print("x:", x)
#b
fig = plt.figure()
ax = plt.axes(projection="3d")
plt.subplots_adjust(bottom=0.1)

t = np.linspace(0, 10, 1000)
xyzs = np.array([x.T @ np.array([np.sin(t[i]), np.cos(t[i]), 1]) for i in range(1000)])

axt = plt.axes([0.05, 0.1, 0.9, 0.03])
st = Slider(axt, "Time", 0, 10)

def update(val):
    ax.clear()
    ax.scatter3D(tqs[:,1], tqs[:,2], tqs[:,3])
    ax.plot3D(xyzs[:,0], xyzs[:,1], xyzs[:,2])
    cval = x.T @ np.array([np.sin(st.val), np.cos(st.val), 1])
    ax.scatter3D(cval[0], cval[1], cval[2], s=100)
st.on_changed(update)

plt.show()