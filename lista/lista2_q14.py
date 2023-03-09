'''14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. Escrever a lista C modificada.'''

import random
def troca_negativo():

    C = []
    Cmodificada = []

    for i in range (10):
        k = random.randint(-100,100)
        C.append(k)
    for k in C:
        if k < 0:
            k = 0
        else:
            pass
        Cmodificada.append(k)
        
    print(f'Lista C: {C}\nLista C modificada: {Cmodificada}')


def main():
    

    troca_negativo()
    

if __name__=='__main__':
    main()

        
        
