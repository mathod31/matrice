from _operator import is_not
from functools import partial

import numpy as np


def matriceH(l: int):
    mat = [] * 7
    for i in range(1, 2 ** l):
        mat.append(np.binary_repr(i, width=l))
        if is_power2(i):
            mat.insert(0, np.binary_repr(i, width=l))
            mat.pop()

    mat = list(zip(*mat))
    newMat = []
    # convert tuple to list
    for m in mat:
        newMat.append(list(m))

    return newMat


def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)


def matriceG(matH, l):
    newIdentity = np.identity(2 ** l - 1 - l, int)
    newMat = []
    newMatSize = 2 ** l - 1 - (2 ** l - 1 - l)
    for m in matH:
        newMat.append(m[newMatSize:])

    matTranspose = np.transpose(newMat).tolist()

    newIdentity = newIdentity.tolist()

    print("new identity = ", newIdentity)
    print("transpose = ", matTranspose)

    matG = []
    cpt = 0
    for m in newIdentity:
        matG.append(m + matTranspose[cpt])
        cpt += 1

    print("mat G = ", matG)

    # print(np.concatenate())

    matTransmpose = np.transpose(newMat)
