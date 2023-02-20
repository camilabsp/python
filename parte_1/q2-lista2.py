'''Escreva um programa de leia o preço de um produto e mostre na tela o valor com 10% de desconto arredondado 
para duas casas decimais.'''

def preco(p):

    d = p - (p * 0.10)

    return d

def main():

    p = float(input('Digite o preço: '))

    print(f'Preço com desconto de 10% : {preco(p):.2f}')


if __name__=='__main__':
    main()
