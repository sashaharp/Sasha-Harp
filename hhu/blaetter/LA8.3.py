import numpy as np
import matplotlib.pyplot as plt

def lepoit(n, x):
    assert type(n) is int, "n ist nicht Ganzzahlig"
    o = np.array([1])
    if n > 0:
        o = np.append(o, [0])
        op = np.array([1])
        for k in range(2, n+1):
            t = np.array(op)
            op = np.array(o)
            o = np.array(np.append(o, 0)*(2*k-1)/(k) - np.append((t*(k-1)/(k))[::-1], [0, 0])[::-1])
    return sum([o[::-1][k]*x**k for k in range(0, len(o))])

def lepore(n, x):
    assert type(n) is int, "n ist nicht Ganzzahlig"
    if(n == 0):
        return 1
    if(n == 1):
        return x
    return x*lepore(n-1, x)*(2*n-1)/n - lepore(n-2, x)*(n-1)/n

print(lepoit(0, 4))
print(lepoit(1, 4))
print(lepoit(2, 4))
print(lepoit(3, 4))

print(lepore(0, 4))
print(lepore(1, 4))
print(lepore(2, 4))
print(lepore(3, 4))

x = np.linspace(-1, 1, 50)

fig = plt.figure(figsize=(10,3))
ax1 = fig.add_subplot(121)
plt.title("Legendre iterativ")
ax2 = fig.add_subplot(122)
plt.title("Legendre rekursiv")

for n in range(0, 6):
    yit = np.array([lepoit(n, xn) for xn in x])
    yre = np.array([lepore(n, xn) for xn in x])
    ax1.plot(x, yit, label="$P_" + str(n) + "(x)$")
    ax2.plot(x, yre, label="$P_" + str(n) + "(x)$")
ax1.legend(prop={'size': 6})
ax2.legend(prop={'size': 6})

plt.show()