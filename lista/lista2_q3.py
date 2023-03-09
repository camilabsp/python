'''3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.'''

import random
def lista_inversa(n):

    I = []

    L = [random.randint(1,100) for i in range(n)]

    I = L[::-1]

    return f'Sequência de {n} números: {L}\nOrdem inversa: {I}'


def main():

    while True:
        try:
            n = int(input('Digite a quantidade de números da sequência: '))
            if n > 0:
                print(lista_inversa(n))
                break
            else:
                print('O valor deve ser maior que 0.')
        except:
            print('Sequência inválida. Tente Novamente!\n')

if __name__=='__main__':
    main()

    
