'Escreva um programa que leia um número inteiro “x” e escreva o valor desse número elevado ao cubo.'

def cubo(x):

    return x**3


def main():

    x = float(input('Digite o valor de x: '))

    print(f' x ao cubo(x³) = {cubo(x):.1f}')


if __name__=='__main__':
    main()

          
