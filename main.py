import encrypt
import time

if __name__ == '__main__':
    start_time = time.time()
    l = 3
    motToDecode = '1011101100011000110011111010001110000111011011111'
    matriceH = encrypt.matriceH(l)
    print('matriceH = ')
    print(matriceH)
    print('\n')

    matriceG = encrypt.matriceG(matriceH, l)
    print('matriceG = ')
    print(matriceG)
    print('\n')

    toEncode = '1100'
    encode = encrypt.encode(matriceG, toEncode)
    print("mot :", toEncode, ", encodé --> ", encode)
    print('\n')

    toModify = '1100101'
    bruitage = encrypt.bruitage(toModify)
    print("mot : ", toModify, ", bruitage --> ", ''.join(bruitage))
    print('\n')

    # encrypt.correction(matriceH, '0011101')
    encrypt.hachage(matriceH, '1011101100011000110011111010001110000111011011111', l)
    print("--- %s seconds ---" % (time.time() - start_time))
