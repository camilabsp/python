'''16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
Escrever as listas X e Y.'''

import random
def lista_indices():

    X = []
    Y = []

    for i in range(10):
        k = random.randint(0,100)
        if i % 2 == 0:
            v = k/2
        else:
            v = k/3

        X.append(k)
        Y.append(round(v,2))
        
    print(f'Lista  X: {X}\nLista Y: {Y}')
    

def main():

    lista_indices()

if __name__=='__main__':
    main()
