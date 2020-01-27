import encrypt
import time

if __name__ == '__main__':
    start_time = time.time()
    l = 3
    matriceH = encrypt.matriceH(l)
    print(matriceH)
    matriceG = encrypt.matriceG(matriceH, l)

    print("--- %s seconds ---" % (time.time() - start_time))
