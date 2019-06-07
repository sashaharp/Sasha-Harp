import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.linspace(0, 10, 2000)
y = np.linspace(0, 10, 2000)
xx, yy = np.meshgrid(x, y)

z = []
with open("result", "r") as f:
    for Y in range(len(y)):
        z.append([])
        l = f.readline().split(";")
        for X in range(len(x)):
            z[Y].append(float(l[X]))

z = np.array(z)
ax.plot_surface(xx, yy, z, cmap=cm.coolwarm)
plt.show()
