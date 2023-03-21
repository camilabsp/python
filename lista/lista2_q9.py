'''9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.'''

import random
def lista_inversa():

    X = []
    Y = []

    for i in range(5):
        x = random.randint(-50,50)
        X.append(x)

        Y = X[::-1]
        

    print(f'Lista X: {X}\nLista Y: {Y}')

def main():

    lista_inversa()


if __name__=='__main__':
    main()
