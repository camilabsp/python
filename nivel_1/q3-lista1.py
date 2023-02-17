'Escreva um programa que leia dois números e mostre na tela a soma e a multiplicação deles.'

def soma (n1,n2):

    soma = n1 + n2

    return soma

def produto(n1,n2):

    produto = n1 * n2

    return produto


def main():

    n1 = float(input('Digite o 1° número: '))
    n2 = float(input('Digite o 2° número: '))

    print(f'A soma é: {soma(n1,n2):.2f} e o produto: {produto(n1,n2):.2f}')

if __name__=='__main__':
    main()
