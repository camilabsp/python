"LISTA 1 - Q9"

def soma(n1,n2):

    soma = 0

    for i in range(n1,n2+1):
        soma += i

    return soma

def main():

    while True:
        try:

            n1 = int(input('Digite o 1° número: '))
            n2 = int(input('Digite o 2° número: '))

            if n1 < n2:
                print(f'A soma do intervalo informado é:',soma(n1,n2))
                
            else:
                print(f'O 2°número deve ser maior que o 1°. Tente Novamente!' )

        except:
            print('Inválido. Tente novamente!')


if __name__=='__main__':
    main()
