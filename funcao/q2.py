"LISTA 1 - Q2"

def area(r):

    a = 3.14 * (r**2)

    return a


def perimetro(r):

    p = 3.14 * 2 * r

    return p


def main():

    while True:
        try:
            r = float(input('Digite o valor do raio (cm): '))
            print(f' A área do círculo é {area(r):.2f} e o perímetro é {perimetro(r):.2f}.')
        except:
            print('Valor do raio inválido. Tente Novamente!')


if __name__=='__main__':
    main()
