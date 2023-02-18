'''Escreva um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostra na tela a idade dessa pessoa 
expressa apenas em dias.'''

def idade(a,m,d):

    dias = (a * 365) + (m * 30) + d

    return dias

def main():

    a = int(input('Quantos anos de vida você tem? '))
    m = int(input('Quantos meses de vida você tem? '))
    d = int(input('Quantos dias de vida você tem? '))

    print(f'Você tem {idade(a,m,d)} dias de vida.')


if __name__=='__main__':
    main()
