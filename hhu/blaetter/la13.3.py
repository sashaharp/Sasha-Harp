import numpy as np
import scipy.linalg as la

def findeEW(A, tol, N):
    assert np.allclose(A, A.T), "not symmetrical!"
    v = np.random.rand(A.shape[0])
    l = 0
    for n in range(N):
        v = (A@v)/la.norm(A@v)
        l = v.T@A@v
        if la.norm(A@v-l*v)<tol:
            return v, l
    print("kein eigenwert unter der Toleranz", tol, "mit", N, "Iterationen gefunden")

m1 = np.diag([10]+[1]*(20-1))
m2 = np.diag([10,9]+[1]*(20-2))

print(findeEW(m1, 10**(-5), 20))
print("Vergleich:")
print(la.eig(m1)[0][0], la.eig(m1)[1][0], "\n\r")
print(findeEW(m2, 10**(-5), 20))
print("Vergleich:")
print(la.eig(m2)[0][0], la.eig(m2)[1][0], "\n\r")