"LISTA 1 - Q5"

def peso_ideal(h,s):

    peso_homem = (72.7 * h) - 58
    peso_mulher = (62.1 * h) -44.7

    if s == 1:
        return peso_homem
    if s == 2:
        return peso_mulher


def main():

    while True:
        try:
            h = float(input('Qual é a sua altura?(m) '))
            s = int(input('Sexo(1:Feminino 2: Masculino): '))
            print(f'Seu peso ideal é: {peso_ideal(h,s):.1f} Kg')
        except:
            print('Inválido. Tente novamente!')


if __name__=='__main__':
    main()
