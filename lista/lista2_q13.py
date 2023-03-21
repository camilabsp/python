'''13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
cada face. '''

import random
def dado(n):

    D = []
    
    f1 = 0
    f2 = 0
    f3 = 0
    f4 = 0
    f5 = 0
    f6 = 0

    for i in range(n):
        d = random.randint(1,6)
        D.append(d)

    for d in D:

        if d == 1:
            
            f1 += 1

        if d == 2:
            
            f2 += 1

        if d == 3:
            
            f3 += 1

        if d == 4:
            
            f4 += 1

        if d == 5:
            
            f5 += 1

        if d == 6:
            
            f6 += 1
            
    print(D)
    print(f'Face 1 - N°ocorrência: {f1}\nFace 2 - N°ocorrência: {f2}\nFace 3 - N°ocorrência: {f3}')
    print(f'Face 4 - N°ocorrência: {f4}\nFace 5 - N°ocorrência: {f5}\nFace 6 - N°ocorrência: {f6}')


def main():

    while True:
        try:
            n = int(input('Número de lançamentos: '))
            if n > 0:
                dado(n)
                break
                
            else:
                print('\nNúmero de lançamentos inválido. Tente Novamente!\n')
            
        except:
            print('\nDigite um valor válido.\n')


if __name__=='__main__':
    main()
