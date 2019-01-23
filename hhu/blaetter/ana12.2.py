import numpy as np

def QR(A):
    alpha = []
    R = A.astype('float').copy()
    m, n = A.shape
    Q = np.eye(m)
    for k in range(n):
        v = R[k:, [k]] 
        # Achtung: R[k:, [k]] ist ein Array der GrÃ¶ÃŸe (m-k, 1).
        # Dagegen ist R[k:, k] ein Array der GrÃ¶ÃŸe (m-k, ).
        alpha.append(-np.sign(R[k, k])*np.linalg.norm(v))
        if alpha[k] == 0:
            alpha[k] = -np.linalg.norm(v)
        e1 = np.eye(m-k, 1)
        u = v - alpha[k]*e1
        Qk = np.eye(m)
        Qk[k:, k:] = np.eye(m-k) - (u @ u.T)/(alpha[k]*(alpha[k] - R[k, k]))
        for j in range(k+1, n):
            R[k:, [j]] = R[k:, [j]] - (R[k:, [j]].T @ u)*u / (alpha[k]*(alpha[k]-R[k, k]))  
        R[k:, [k]] = alpha[k]*e1
        Q = Q @ Qk
    return alpha

print(QR(np.array([[1,2,3],[4,5,6],[7,8,10]])))