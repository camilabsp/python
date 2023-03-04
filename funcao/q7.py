"LISTA 1 - Q7"

def fatorial(n):
    
    f = 1
    for  i in range(1,n+1):
        f = f*i
    
    return f

def main():

    while True:
        try:
            n = int(input('Digite um número: '))
            print(f'O fatorial de {n} é: {fatorial(n)}')
        except:
            print('Número inválido. Tente novamente!')

if __name__=='__main__':
    main()
