"LISTA 1 - Q12"

def somatorio(n):

    soma = 0

    for i in range(0,n+1):
        soma += i
    return soma


def main():

    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            if n < 0:
                print('Número inválido. Tente novamente!')
            else:
                print(f'O somatório de {n} é: {somatorio(n)}.')
        except:
            print('Número inválido. Tente novamente!')


if __name__=='__main__':
    main()

