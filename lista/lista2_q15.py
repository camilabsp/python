'''15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E.'''

import random
def lista_inversa():

    D = []
    E = []

    for i in range(10):
        k = random.randint(-100,100)
        D.append(k)
        E = D[::-1]

    print(f'Lista D: {D}\nLista E: {E}')


def main():

    lista_inversa()


if __name__=='__main__':
    main()
        
    
