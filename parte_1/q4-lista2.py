'Escreva um programa que leia uma quantidade de minutos e mostre a quantidade de horas e minutos equivalente.'

def horas(m):

    horas = m // 60

    return horas


def minutos(m):

    minutos = m % 60

    return minutos


def main():

    m = int(input('Digite a quantidade de minutos: '))

    print(f'{m} minutos equivalem a {horas(m)} hora(s) e {minutos(m)} minuto(s).')


if __name__=='__main__':
    main()
