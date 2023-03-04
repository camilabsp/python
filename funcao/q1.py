"LISTA 1 - Q1"

def par_impar(n):

    if n % 2 == 0:
        return True
    else:
        return False

def main():
    
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            if par_impar(n) == True:
                print(f'{n} é par')
            else:
                print(f'{n} é ímpar')
        except:
            print('Número inválido. Tente novamente!')
            


if __name__=='__main__':
    main()
