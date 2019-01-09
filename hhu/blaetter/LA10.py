import numpy as np
def  LR_kompakt(A): #:
    A = A.astype(float).copy() #no ""
    n = A.shape[0]
    p = np.arange(n) #np
    for kk in range(n):
        ll = kk + np.flatnonzero(A[kk:, kk ])[0] #()
        A[ [kk , ll] ] = A[ [ll , kk] ]
        p[ [kk , ll] ] = p[ [ll , kk] ]
        A[kk+1:, kk] /= A[kk , kk]
        A[kk+1:, kk+1:]  -= A[kk+1:,  kk ] @ A[ kk , kk+1:]
    return p

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)
print(LR_kompakt(A))
print(LR_kompakt(A)@A)