"LISTA 1 - Q10(A)"

def maximo(n1,n2):

    if n1 > n2:
        return n1
    else:
        return n2
    

def main():

    while True:
        try:
            n1 = int(input('Digite o 1°número: '))
            n2 = int(input('Digite o 2°número: '))
            print(f'O maior número é {maximo(n1,n2)}')
        except:
            print('Número inválido. Tente novamente!')

if __name__=='__main__':
    main()
