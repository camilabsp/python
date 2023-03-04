"LISTA 1 - Q13"

def somatorio(n):

    s = 0

    for i in range(1,n+1):
        
        s = s + (1/i)

    return s


def main():
    
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            if n < 0:
                print('Número inválido. Tente novamente')
            else:
                print(f'S é igual a {somatorio(n):.1f}')
        except:
            print('Número inválido. Tente novamente!')
            


if __name__=='__main__':
    main()
