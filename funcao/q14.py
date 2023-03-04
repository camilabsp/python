"LISTA 1 - Q14"

def somatorio_fatorial(n):

        s = 0

        f = 1

        for i in range(1,n+1):

                f = f * i

                s = 1 + 1 + (1/2) + (1/6) + (1/f)

        return s


def main():

        while True:
                try:
                    n = int(input('Digite um número: '))
                    print(f' O valor de S é: {somatorio_fatorial(n):.2f}')
                except:
                        print('Número inválido. Tente novamente!')


if __name__=='__main__':
    main()

