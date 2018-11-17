import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 500)

y = 1/((x-4)**2*(x-1))

b1 = x < 1
b2 = [(b > 1 and b < 4) for b in x]
b3 = x > 4

plt.plot(x[b1], y[b1])
plt.plot(x[b2], y[b2])
plt.plot(x[b3], y[b3])

plt.show()