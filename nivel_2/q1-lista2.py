'''Escreva um programa que leia dois valores e mostre na tela, nessa ordem:

a. A soma dos números;
b. A concatenação das strings;
c. A multiplicação dos números;
d. A multiplicação como strings;
e. A divisão dos números;
f. A divisão inteira dos números;
g. A exponenciação;
h. O módulo (resto)'''

def soma(n1,n2):

    soma = n1 + n2

    return soma

def concatena(n1,n2):

    concatenacao = str(n1) + str(n2)

    return concatenacao

def produto(n1,n2):

    produto = n1 * n2

    return produto

def strin(n1,n2):

    str1 = str(n1)
    str2 = str(n2)

    return str1 + '*' + str2

def divisao(n1,n2):

    div = n1/n2

    return div

def div_inteira(n1,n2):

    div_inteira = n1//n2

    return div_inteira

def exp(n1,n2):

    expo = n1**n2

    return expo

def resto(n1,n2):

    resto = n1 % n2

    return resto


def main():

    n1 = int(input('Digite o 1° valor: '))
    n2 = int(input('Digite o 2° valor: '))

    print('Soma dos números: ',soma(n1,n2))
    print('Concatenação das strings: ',concatena(n1,n2))
    print('Multiplicação dos números: ',produto(n1,n2))
    print('Multiplicação como strings: ',strin(n1,n2))
    print('Divisão dos números: ',divisao(n1,n2))
    print('Divisão inteira dos números: ',div_inteira(n1,n2))
    print('Exponenciação: ',exp(n1,n2))
    print('Módulo(resto): ',resto(n1,n2))


if __name__=='__main__':
    main()
                

    
