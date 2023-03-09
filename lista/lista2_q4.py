'''4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.'''

import random
def posicoes():

    L = []
    maior = 0
    menor = 0

    for i in range(15):
        posicao = i + 1
        k = random.randint(0,100)
        L.append(k)
        
        for k in L:
            if k == 0:
                maior = menor = 0
            else:
                if k > maior:
                    maior = k
                    print(i,maior)
                if k < menor:
                    menor = k
                    print(i,menor)

  
def main():

    posicoes()


if __name__=='__main__':
    main()
