'''Escreva um programa que leia um valor inteiro e mostra na tela no valor booleano True caso o número lido seja maior que 
100 ou False caso contrário'''

def true_false(n):

    if n > 100:

        return True

    else:

        return False


def main():

    n = int(input('Digite um número inteiro: '))

    print(true_false(n))


if __name__=='__main__':
    main()
