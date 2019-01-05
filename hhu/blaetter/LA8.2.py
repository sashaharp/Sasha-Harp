import numpy as np

def mydet(A):
    assert A.shape[0] == A.shape[1], "Die Matrix ist nicht quadratisch"
    if(A.shape == (2, 2)):
        return A[0, 0]*A[1, 1]-A[0, 1]*A[1, 0]
    if(A.shape == (1, 1)):
        return A[0, 0]
    return sum([A[0, i]*(-1)**(i+1)*mydet(np.concatenate((A[1::,:i:], A[1::,i+1::]), axis=1)) for i in range(0, A.shape[0])])

#print(mydet(np.ones(4).reshape(2,2)))
A = np.array([1, 3, 2, 0, 1, 1, 2, 3, 4, 0, 8, 3, 2, 5, 4, 5]).reshape(4, 4)
B = np.array([4, 5, 6, 6, 7, 7, 9, -3, 8, 4, 0, -7, -5, 3, -6, -4]).reshape(4, 4)
C = np.array([1, 2, 3, 4])
#print(np.concatenate((A[1::,:2:], A[1::,3::]), axis=1))
print(mydet(A), np.linalg.det(A))
print(mydet(B), np.linalg.det(B))
print(mydet(C), np.linalg.det(C))