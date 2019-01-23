#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#SIE SOLLEN DIESE DATEI IMPORTIEREN, Ã¶ffnen zum Durchlesen schadet aber nicht.

import numpy as np
from bruchpy import Bruch

def TestLR_Bruch(testfunktion):
    m = 10
    print('Ihre Funktion wird jetzt mit 3 ({0}x{0})-Matrizen getestet'.format(m));
    A = _zufallsmatINT(m)
    B = _zufallsmatBRUCH(m)
    C1 = _zufallsmatINT(m)
    C = _zufallsmatBRUCH(m)
    for i in range(m):
        for j in range(m):
            zufallsindex = np.random.randint(0,2)
            if zufallsindex == 0:
                C[i, j] = C1[i, j]
    texte = ['Matrix mit Integer-EintrÃ¤gen',\
             'Matrix mit Bruch-EintrÃ¤gen',\
             'Matrix mit gemischten EintrÃ¤gen']
    tb = 0
    for M, text in zip([A, B, C], texte):
        print('Teste ' + text + ':')
        p, MLR = testfunktion(M)
        R = np.triu(MLR)
        L = np.eye(MLR.shape[0], dtype=int) + np.tril(MLR, -1)
        erg = np.equal(M[p,:],np.dot(L,R)).all()
        print("Das Ergebnis ist {0}.".format(erg));
        if erg:
            tb += 1;
    
    print('{0} von {1} Tests erfolgreich'.format(tb, 3));

def _zufallsmatINT(m, Null = True):
    mat = np.random.randint(-20,20, m**2)
    if Null == False:
        mat[mat == 0] += 1
    return mat.reshape(m,m)

def _zufallsmatBRUCH(m):
    ZufINT1 = _zufallsmatINT(m)
    ZufINT2 = _zufallsmatINT(m, Null = False)
    MatBRUCH = np.zeros((m,m), dtype=Bruch)
    for i in range(m):
        for j in range(m):
            MatBRUCH[i,j] = Bruch(int(ZufINT1[i,j]), int(ZufINT2[i,j]))
    return MatBRUCH


def QbTest(testfunktion):
    m, n = 20, 15
    print('Ihre Funktion wird jetzt mit einer ({0}x{0})- '.format(m)\
          +'und einer ({0}x{1})-Matrix getestet'.format(m, n));
    t = 0
    for mm, nn in zip([m, m], [m, n]):   
        Vtest = np.tril(np.random.rand(mm, nn))
        Vtest = Vtest/np.linalg.norm(Vtest, axis=0)
        btest = np.random.rand(mm,1)
        Qb1 = testfunktion(Vtest, btest)
        Qb2 = _Qblang(Vtest, btest)
        if np.allclose(Qb1, Qb2):
            t += 1
    print('{0} von {1} Tests erfolgreich'.format(t, 2));
    
def _Qblang(V, b):
    m, n = V.shape
    Q = np.eye(m)
    for k in range(n):
        v = V[k:, [k]]
        Qk = np.eye(m)
        Qk[k:, k:] = np.eye(m-k) - 2*(v @ v.T)
        Q = Q @ Qk
    return Q@b