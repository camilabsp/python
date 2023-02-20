'''Escreva um programa que leia dois valores, um dividendo e um divisor. Mostre o resultado da divisão e o resto da 
divisão inteira dos valores'''

def divisao_inteira(n1,n2):

    resto = n1 % n2

    return resto


def main():

    n1 = int(input('Digite o dividendo: '))
    n2 = int(input('Digite o divisor: '))

    print(f'O resto da divisão inteira é: {divisao_inteira(n1,n2)}')


if __name__=='__main__':
    main()
