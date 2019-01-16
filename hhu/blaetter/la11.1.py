import numpy as np
def GS(A):
    B = [] #wegen sum
    B.append(A[0])
    for i in range(1, len(A)):
        s = 0
        for j in range(i):
            p=sum(A[i]*np.array(B[j]))/sum(np.array(B[j])**2)
            s+=p*np.array(B[j])
        B.append(A[i]-s)
    return(B)
Tom = np.array([[3, 1],[2, 2]])
Tom = GS(Tom)
print(Tom)

def GS_mod(A)