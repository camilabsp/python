"LISTA 1 - Q11"

def divisor(n):
    
    soma = 0
    
    for i in range(1,n+1):
        if n % i == 0:
            qtd = 1
            soma += qtd
        
    return soma


def main():

    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            if n <= 0:
                print('Número inválido. Tente novamente!')
            else:
                print(f'O número {n} tem {divisor(n)} divisores.')
            
        except:
            print('Número inválido. Tente novamente!')


if __name__=='__main__':
    main()

