import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
xn = np.linspace(-100, 100, 50)
yn = np.linspace(-100, 100, 50)
x, y = np.meshgrid(xn, yn)
h = x**3 + y**3 - 3*x*y
b = (xn**3 + yn**3 - 3*xn*yn == 0)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(x, y, h, cmap=plt.cm.viridis, rstride=1, cstride=1, linewidth=2)
#plt.savefig('test1.pdf')
plt.plot(xn[b], yn[b])
plt.show()