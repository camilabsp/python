'''17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
aparece.'''

import random
def posicao_indice(v):

    W = []
    c = 0

    for i in range(10):
        k = random.randint(1,10)
        W.append(k)
    
        if v == k:
            c +=1
            
        else:
            pass

    print(f'Lista W: {W}\nO número {v} aparece na lista {c} vez(es).')

    
def main():
    
    while True:
        try:
            v = int(input('Digite um valor: '))
            if v > 0:
                posicao_indice(v)
            else:
                print('O valor deve ser maior que 0. Tente novamente!')

        except:
            print('Valor inválido. Tente novamente!')


if __name__=='__main__':
    main()
