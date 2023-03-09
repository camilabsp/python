'''18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.'''

import random
def lista_negativos():

    X = []
    R = []
   

    for i in range(10):
        k = random.randint(-100,100)
        X.append(k)
    for k in X:
        if k < 0:
            R.append(k)

        else:
            pass

    print(f'Lista X: {X}\nLista R: {R}')


def main():


    lista_negativos()


if __name__=='__main__':
    main()

    
