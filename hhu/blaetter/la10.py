import numpy as np  #sinnvolle Zeile Nr. 1
    #sinnvolle Zeile Nr. 2
def LR_kompakt(A): #funktion    #sinnvolle Zeile Nr. 3
    A = A.astype(float).copy() #kein string #sinnvolle Zeile Nr. 4
    n = A.shape[0]  #sinnvolle Zeile Nr. 5
    p = np.arange(n)#np #sinnvolle Zeile Nr. 6
    for kk in range(n-1): #sinnvolle Zeile Nr. 7
        ll = kk + np.flatnonzero(A[kk:, kk])[0]#funktion    #sinnvolle Zeile Nr. 8
        A[[ kk, ll ]] = A[[ ll, kk ]]   #sinnvolle Zeile Nr. 9
        p[[ kk, ll ]] = p[[ ll, kk ]]#<->   #sinnvolle Zeile Nr. 10
        A[kk+1:, kk] /= A[kk, kk]   #sinnvolle Zeile Nr. 11
        A[kk+1:, kk+1:] -= A[kk+1:, [ kk ]] @ A[[ kk ], kk+1:]  #sinnvolle Zeile Nr. 12
    return p, A    #sinnvolle Zeile Nr. 13

def LR_kompakt_2(A): #funktion    #sinnvolle Zeile Nr. 3
    A = A.astype(float).copy() #kein string #sinnvolle Zeile Nr. 4
    n = A.shape[0]  #sinnvolle Zeile Nr. 5
    p = np.arange(n)#np #sinnvolle Zeile Nr. 6
    for kk in range(n-1): #sinnvolle Zeile Nr. 7
        ll = kk + np.argmax(abs(A[kk:, kk]))#funktion    #sinnvolle Zeile Nr. 8 #rundungsfehler minimiert
        A[[ kk, ll ]] = A[[ ll, kk ]]   #sinnvolle Zeile Nr. 9
        p[[ kk, ll ]] = p[[ ll, kk ]]#<->   #sinnvolle Zeile Nr. 10
        A[kk+1:, kk] /= A[kk, kk]   #sinnvolle Zeile Nr. 11
        A[kk+1:, kk+1:] -= A[kk+1:, [ kk ]] @ A[[ kk ], kk+1:]  #sinnvolle Zeile Nr. 12
    return p, A    #sinnvolle Zeile Nr. 13


A1 = np.array([[1,2,3],[4,5,6],[7,8,10]])
A2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A1.copy())
p, B = LR_kompakt(A1.copy())
print(B, p)
p, B = LR_kompakt_2(A1.copy())
print(B, p)

print(A2)
p, B = LR_kompakt(A2.copy())
print(B, p)
p, B = LR_kompakt_2(A2.copy())
print(B, p)