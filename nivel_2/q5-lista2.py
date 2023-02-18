''' Escreva um programa que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é 
ponderada e que o peso das notas são 2, 3 e 5.'''

def media_ponderada(n1,n2,n3):

    media_pond = ((n1*2)+(n2*3)+(n3*5))/10

    return media_pond


def main():

    n1 = float(input('Digite a 1ª nota: '))
    n2 = float(input('Digite a 2ª nota: '))
    n3 = float(input('Digite a 3ª nota: '))

    print(f'A média ponderada é: {media_ponderada(n1,n2,n3):.1f}')

if __name__=='__main__':
    main()



    

    
