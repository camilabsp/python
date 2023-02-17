def comprimento(r):

    pi = 3.14

    c = 2 * pi * r

    return c

def area_circulo(r):

    pi = 3.14

    a = pi * (r**2)

    return a

def area_esfera(r):

    pi = 3.14

    ae = 4 * pi * (r**2)

    return ae

def volume_esfera(r):

    pi = 3.14

    v = (4/3) * pi * (r**3)

    return v
    


def main():

    r = float(input('Digite o valor do raio: '))
    print(f'O comprimento da circunferência é: {comprimento(r):.6f}')
    print(f' A área do círculo é: {area_circulo(r):.6f}')
    print(f'A área da esfera é:{area_esfera(r):.6f}')
    print(f'O volume da esfera é: {volume_esfera(r):.6f}')


if __name__=='__main__':
    main()
