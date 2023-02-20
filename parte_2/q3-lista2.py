'Escreva um programa que leia uma temperatura em graus Celsius e mostra na tela o valor correspondente em graus Fahrenheit'

def fahrenheit(c):

    f = (c * (9/5)) + 32

    return f


def main():

    c = float(input('Digite a temperatura em Celsius: '))

    print(f'A temperatura em Fahrenheit é: {fahrenheit(c):.1f} °F')


if __name__=='__main__':
    main()
