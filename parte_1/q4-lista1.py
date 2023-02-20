' Escreva um programa que ler o valor da variável x. Calcule e mostre o resultado da expressão: 9x - 4x + 10'

def equacao(x):

    e = (9 * x) - (4 * x) + 10

    return e


def main():

    x = float(input('Digite o valor de x: '))
    print(f' O valor de x é {equacao(x)}')

if __name__=='__main__':
    main()
