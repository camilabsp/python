'Escreva um programa que leia três números inteiros nas variáveis “a”, “b” e “c” e escreva a média deles.'

def media(a,b,c):

    media = (a + b + c)/3

    return media


def main():

    a = int(input('Digite o valor da variável a: '))
    b = int(input('Digite o valor da variável b: '))
    c = int(input('Digite o valor da variável c: '))

    print(f' A média dos valores é: {media(a,b,c):.2f}')


if __name__=='__main__':
    main()
    
    
    
