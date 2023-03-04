"LISTA 1 - Q6"

def triangulo(l,m):
    p = l * m
    return f'TRIÂNGULO\nO perímetro equivale a {p:.2f}cm.'
    
def quadrado(l,m):
    a = m**2
    return f'QUADRADO\nA área equivale a {a:.2f}cm²'

def pentagono(l):    
    return 'PENTÁGONO'


def main():

    while True:
        try:
            l = int(input('Quantidade de lados: '))
            if l < 3 or l > 5:
                print('Valor inválido. Tente Novamente!')
            else:
                m = float(input('Quanto mede o lado?(cm) '))
                if l == 3:
                    print(triangulo(l,m))
                elif l == 4:
                    print(quadrado(l,m))
                elif l == 5:
                    print(pentagono(l))
    
        except:
            print('Valor inválido. Tente Novamente!')


if __name__=='__main__':
    main()
