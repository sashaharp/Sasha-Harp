import numpy as np
def QRZerlegung(R):
    n = len(R)
    m = len(R[0])
    Qn = np.identity(n)
    for k in range(1, n+1):
        a = -1*np.sign(R[k-1,k-1])*np.sqrt(sum(R[k-1:,k-1]*sum(R[k-1:,k-1])))
        e = np.zeros(m-k+1)
        e[0] = 1
        u = R[k-1:, k-1] - a*e
        tempQ = np.identity(m-k+1) - u*u.T/(a*(a-R[k-1,k-1]))
        Q = np.append(np.append(np.identity(k-1), np.zeros((k-1)*(m-k+1)).reshape(k-1, m-k+1), axis=1), np.append(np.zeros((k-1)*(m-k+1)).reshape(m-k+1, k-1), tempQ, axis=1), axis=0)
        for j in range(k, n):
            R[k-1:,j] = R[k-1:, j] - u*sum(R[k-1:,j]*u)/(a*(a-R[k-1, k-1]))
        R[k-1:, k-1] = a*e
        Qn=Qn@Q
    return Qn, R

Q, R = QRZerlegung(np.array([[1,2,3],[4,5,6],[7,8,10]]))
print(Q, R)
print(Q@R)