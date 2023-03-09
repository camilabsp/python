'''2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos dessa lista.'''

import random
def lista():

    negativos = 0
    soma = 0

    L = [random.randint(-100,100)for i in range(10)]

    for k in L:
        if k < 0:
            negativos += 1

        elif k > 0:
            soma += k

    print(f'Quantidade de números negativos: {negativos}\nSoma dos números positivos: {soma}')


def main():

    lista()


if __name__=='__main__':
    main()
