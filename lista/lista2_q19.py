'''19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
de S. Escrever a lista X.'''

import random
def lista():

    R = []
    S = []
    X = []

    for i in range (5):
        r = random.randint(-100,100)
        R.append(r)

    for i in range (10):
        s = random.randint(-100,100)
        S.append(s)


    X = R + S


    print(X)


def main():


    lista()


if __name__=='__main__':
    main()

    
    
