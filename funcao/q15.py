'LISTA 1 - Q15'
'''Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)'''

def soma(n):
    s = 0
    for t in range (1,n+1):
        numerador = t**2 + 1
        denominador = t + 3
        s += numerador/denominador
    return s

def main():

    while True:
        try:
            n = int(input('Digite a quantidade de termos: '))
            if n < 0:
                print('Valor negativo. Tente novamente!')
            else:
                print(f'A soma é: {soma(n):.2f}')
                break
        except:
            print('Valor inválido. Tente novamente!')


if __name__=='__main__':
    main()
