"LISTA 1 - Q10b"

def max_numero(n1,n2,n3,n4):
    
        if (n1 > n2 and n1 > n3 and n1 > n4) or (n1 == n2 and n1 > n3 and n1 > n4) or (n1 == n3 and n1 > n2 and n1 > n4) or (n1 == n4 and n1 > n2 and n1 > n3) or (n1 == n2 == n3 and n1 > n4):

                return n1

        if (n2 > n1 and n2 > n3 and n2 > n4) or (n2 == n3 and n2 > n4 and n2 > n1) or (n2 == n4 and n2 > n1 and n2 > n3):

                return n2

        if (n3 > n1 and n3 > n2 and n3 > n4) or (n3 == n4 and n3 > n1 and n3 > n2):

                return n3

        if (n4 > n1 and n4 > n2 and n4 > n3):

                return n4
                        
                
        

def main():

    while True:
        try:
            for i in range(4):
                n1 = int(input(f'Digite o 1° número da série {i+1}: '))
                n2 = int(input(f'Digite o 2° número da série {i+1}: '))
                n3 = int(input(f'Digite o 3° número da série {i+1}: '))
                n4 = int(input(f'Digite o 4° número da série {i+1}: '))

                if (n1 == n2 == n3 == n4):
                        print('Todos os valores são iguais.')
                else:
                        
                        print(f'O maior número da série {i+1} é: {max_numero(n1,n2,n3,n4)}')

        except:
            print('Número inválido. Tente novamente!')


if __name__=='__main__':
    main()

