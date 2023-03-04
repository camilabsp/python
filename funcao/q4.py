"LISTA 1 - Q4"

def media(n1,n2):

    media = (n1 + n2)/2

    if media >= 6:
        print('PARABÉNS! Você foi aprovado!')
    else:
        print('Você não atingiu a pontuação necessária para aprovação!')

    return media


def main():

    while True:
        try:
            n1 = float(input('Digite a 1ª nota: '))
            n2 = float(input('Digite a 2ª nota: '))
            print(f'Sua média semestral é: {media(n1,n2):.2f}')
        except:
            print('Nota inválida. Tente novamente!')



if __name__=='__main__':
    main()
