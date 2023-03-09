'''5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
elementos deste em uma outra lista de 20 elementos.'''

import random
def listas():

    A = []
    B = []
    C = []

    for i in range(10):
        a = random.randint(0,100)
        b = random.randint(0,100)
        A.append(a)
        B.append(b)

        for i in range(20):

            if i % 2 ==  0:

                i = B[i]

            else:

                i = A[i]

        C.append(i)

    print(A)
    print(B)
    print(C)
    
    
def main():

    listas()


if __name__=='__main__':
    main()
