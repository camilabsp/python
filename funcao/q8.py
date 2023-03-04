"LISTA 1 - Q8"

def cubo(n):
    
    cub = n ** 3

    return cub
    

def main():

    while True:
        try:

            n = int(input('Digite um número inteiro: '))

            print(f'{n}³ é igual a {cubo(n)}')

            msg = input('Deseja continuar? (S-sim N-não) ').upper()

            if msg == 'N':
                print('FIM!')
                break

        except:

            print('Número inválido. Tente novamente!')



if __name__=='__main__':
    main()
