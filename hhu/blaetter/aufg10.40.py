from scipy import linalg as la
import numpy as np
def vorwaerts(L, b):
    assert (L.shape[0] == L.shape[1] and L.shape[0] == b.shape[0] and b.shape[1] == 1),\
    "Dimensions don't fit."
    assert not(any(np.diag(L) == 0)), "L not invertible."
    # Die Überprüfung geht natürlich auch in der Schleife, indem jedes 
    # Diagonalelement überprüft wird.
    n = L.shape[0]
    x = np.zeros_like(b, dtype='float')
    x[0] = b[0]/L[0, 0]
    for i in range(1, n):
        x[i] = 1/L[i, i] * (b[i] - L[[i], :i] @ x[:i])
    return x

# Rückwärtssubstitution 
#(nicht in der Aufgabe gefordert, aber nützlich für Aufgabe 38)
def rueckwaerts(R, b):
    assert (R.shape[0] == R.shape[1] and R.shape[0] == b.shape[0] and b.shape[1] == 1),\
    "Dimensions don't fit."
    assert not(any(np.diag(R) == 0)), "R not invertible."
    # Die Überprüfung geht natürlich auch in der Schleife, indem jedes 
    # Diagonalelement überprüft wird.
    n = R.shape[0]
    x = np.zeros_like(b, dtype='float')
    x[n-1] = b[n-1]/R[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = 1/R[i, i] * (b[i] - R[[i], i+1:] @ x[i+1:])
    return x


def func(A, b):
    P, L, R = la.lu(A)
    Pinv = P.T
    a = vorwaerts(L, Pinv@b)
    x = rueckwaerts(R, a)
    return x

def Aufgabe38(testfunktion):
    '''Aufgabe38 testet automatisch, ob die übergebene Funktion "testfunktion"
    die Anforderungen aus Aufgabe 38 erfüllt.
    Dazu löst es mit "testfunktion" einige lineare Gleichungssysteme
    verschiedener Größe und überprüft das Residuum.
    '''
    print('Ihre Funktion wird jetzt mit 4 Gleichungssystemen getestet');
    print('Wenn die Norm des Residuums klein ist (<10^-8), ist der Test bestanden.')
    
    tb=0
    AsUndBs = [
        (np.array([
            [ 0, 1, 2 ],
            [ 1, 2, 5 ],
            [ 2, 3, 4 ],
        ], dtype = float), np.random.rand(3, 1)),
        _generierteZufallsmatrixMitGuterKonditionUndVektor(5, float),
        _generierteZufallsmatrixMitGuterKonditionUndVektor(100, float),
        _generierteZufallsmatrixMitGuterKonditionUndVektor(100, int),
    ];
    texte = [
        "mit der Matrix\n{0}",
        "einer reellen {0.shape[0]} x {0.shape[1]} Matrix",
        "einer reellen {0.shape[0]} x {0.shape[1]} Matrix",
        "einer komplexen {0.shape[0]} x {0.shape[1]} Matrix",
    ];
    
    tb = 0;
    for (A, b), text in zip(AsUndBs , texte):
        text = text.format(A);
        print("Teste {0}.".format(text));
        x = testfunktion(A.copy(), b);
        residuum = A @ x - b;
        resNorm = np.linalg.norm(residuum);
        print("Die Norm des Residuums ist {0}.".format(resNorm));
        if resNorm < 1e-8:
            tb += 1;
    
    print('{0} von {1} Tests erfolgreich'.format(tb, len(AsUndBs)));


def _generierteZufallsmatrixMitGuterKonditionUndVektor(N, typ):
    """
    Generiert eine Zufallsmatrix vorgegebener Größe und vorgegebenem Typs
    so, dass die Konditionszahl der Matrix gut ist.
    """
    while True:
        # Wir raten so lange Matrizen, bis die Kondition der geratenen Matrix
        # gut ist.
        A = 200 * ((np.random.rand(N, N) - 1/2) * 2);
        A = A.astype(typ);
        if typ == complex:
            # Rate zusätzlichen Imaginärteil
            A += 1j * 200 * ((np.random.rand(N, N) - 1/2) * 2);
        if np.linalg.cond(A) <= N:
            break;
    b = np.random.rand(N, 1);
    return A, b;

Aufgabe38(func)