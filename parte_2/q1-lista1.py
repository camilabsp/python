'''Considere que as variáveis “dia”, “mês” e “ano” contém os valores respectivos de uma certa data. Escreva um comando “print” 
que imprima essa data no formato usado, por exemplo, “15/4/2020” ou “2/12/2004”'''

def dia(d):

    return d

def mes(m):

    return m

def ano(a):

    return a


def main():

    d = int(input('Digite o dia: '))
    m = int(input('Digite o mês: '))
    a = int(input('Digite o ano: '))

    print(f' A data é {dia(d)}/{mes(m)}/{ano(a)}')

if __name__=='__main__':
    main()


    
