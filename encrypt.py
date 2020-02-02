import numpy as np
from random import randrange


def matriceH(l: int):
    mat = [] * 7
    cpt = 2 ** l - 1;
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
    matG = []
    cpt = 0
    for m in newIdentity:
        matG.append(m + matTranspose[cpt])
        cpt += 1

    return matG


def convertMotToMatrix(mot):
    newMot = []
    for i in mot:
        newMot.append(i)

    return newMot


def convertMotEncodeInF2(mat):
    mot = ''
    for m in mat:
        mot += str(m % 2)
    return mot


def convertMotDecodeInF2(mat):
    mot = ''
    for m in mat:
        for i in m:
            mot += str(i % 2)
    return mot


def encode(matG, mot):
    mot = convertMotToMatrix(mot)

    mot = np.array(mot, dtype='int')
    matG = np.array(matG, dtype='int')
    motEncode = mot @ matG
    motEncode = convertMotEncodeInF2(motEncode)
    return motEncode


def modifyBitByPostion(mot, position):
    mot = list(mot)
    newValue = str((int(mot[position]) + 1) % 2)
    mot[position] = newValue
    return mot


def bruitage(mot):
    lenght = len(mot)
    rand = randrange(lenght - 1)
    mot = modifyBitByPostion(mot, rand)

    return mot


def getSyndromePosition(matH, motCorrection):
    numberCol = len(matH[0])
    motCorrection = np.array(list(motCorrection), dtype='int')

    for c in range(0, numberCol):
        if np.array_equal(matH[:, c], motCorrection):
            return c
    return None


def correction(matH, mot):
    motNotModify = mot
    mot = [convertMotToMatrix(mot)]
    motTranspose = np.transpose(mot)

    mot = np.array(motTranspose, dtype='int')
    matH = np.array(matH, dtype='int')

    syndrome = matH @ mot

    syndrome = convertMotDecodeInF2(syndrome)
    syndromePosition = getSyndromePosition(matH, syndrome)
    if syndromePosition is not None:
        motCorrected = modifyBitByPostion(motNotModify, syndromePosition)
    else:
        motCorrected = 'Correct Word'

    print(motNotModify, " --> ", ''.join(motCorrected))


def hachage(matH, motEncode, l):
    length = len(motEncode)
    sizeCut = 2 ** l - 1
    mots = [motEncode[y - sizeCut:y] for y in range(sizeCut, len(motEncode) + sizeCut, sizeCut)]
    print('mots hashés : ', mots)
    print('décodage :')
    for mot in mots:
        correction(matH, mot)
