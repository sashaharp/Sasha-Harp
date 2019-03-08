import locale
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

#for thousand separators:
locale.setlocale(locale.LC_NUMERIC, "en_US.UTF-8")

t = []
f = []

#loop through file
with open("a49.dat") as file:
    for l in file.readlines():
        t.append(locale.atof(l.split(" ")[0]))
        f.append(locale.atof(l.split(" ")[1]))

t = np.array(t)
f = np.array([f]).T

#algo
A = np.vstack([np.exp(t), np.exp(-1*t), t**2, np.ones(len(t))]).T

x = la.solve(A.T@A, A.T@f)

print("x:", x)

#waht?
def QR_kompakt(A):
    ''' Berechnet die QR-Zerlegung der Matrix Aâ‚¬R^{mxn}
    Input: Matrix A
    Output: alphas, neues Array mit vs und teilweis#algo
A = np.vstack([np.exp(t), np.exp(-1*t), t**2, np.ones(len(t))]).T

x = la.solve(A.T@A, A.T@f)

print("x:", x)
    '''
    V = A.astype('float').copy()
    m, n = A.shape
    alphas = np.zeros(n)
    for k in range(n):
        u = V[k:, [k]] 
        alpha = -np.sign(V[k, k])*np.linalg.norm(u)#algo
A = np.vstack([np.exp(t), np.exp(-1*t), t**2, np.ones(len(t))]).T

x = la.solve(A.T@A, A.T@f)

print("x:", x)
        if alpha == 0:
            alpha = -np.linalg.norm(u)
        alphas[k] = alpha
        u -= alpha*np.eye(m-k, 1)
        for j in range(k+1, n):
            V[k:, [j]] -= (V[k:, [j]].T @ u)*u/(alpha*(alpha-V[k, k]))
        V[k:, [k]] = u / np.linalg.norm(u)
        # oder das gleiche, ohne den Befehl np.linalg.norm: 
        #V[k:, [k]] = u / np.sqrt(2*alpha*(alpha - V[k, k]))
    return alphas, V 

def Qprodb(V, a):
    b = a.astype('float').copy()
    n = V.shape[1]
    for k in range(n-1,-1,-1):
        # wichtig: durch Vertauschen erhalten wir Skalarprodukt * Vektor:
        b[k:] = b[k:] - 2*(V[k:,[k]].T @ b[k:]) * V[k:,[k]]
    return b


#c
tf = np.array([t, f.reshape(9)]).T
tf = tf[tf[:,0].argsort()]
plt.plot(tf[:,0], tf[:,1])
plt.plot(tf[:,0], tf[:,1], "+r")
ts = np.linspace(-2, 2, 400)
f = x[0]*np.exp(ts)+x[1]*np.exp(-1*ts)+x[2]*ts**2+x[3]
plt.plot(ts, f)
plt.show()