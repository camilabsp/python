'''10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra'''

import random
def lista_posicao():

    L = []
    menor = 0
    maior = 0

    for i in range(15):
        k = random.randint(-100,100)
        L.append(k)

    for L[i] in L:

        if L[i] == 0:
            maior = menor = 0

        else:

            if L[i] > maior:
                maior = L[i]
                p_maior = L.index(maior) + 1
                
 
            elif L[i] < menor:
                menor = L[i]
                p_menor = L.index(menor) + 1
                    
    print(L)
    print(f'Maior elemento é o {maior} na posição {p_maior}\nMenor elemento é o {menor} na posição {p_menor}')
   
            

def main():

    lista_posicao()


if __name__=='__main__':
    main()
