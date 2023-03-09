'''7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
outro valor dado pertence ou não à lista.'''

import random
def lista(n):

    L = []

    for i in range(10):
        k = random.randint(-50,50)
        L.append(k)
    
    if n in L:
        print(f'Lista: {L}\nO número {n} pertence à lista.')
    else:
        print(f'Lista: {L}\nO número {n} não pertence à lista.')
    

def main():

    while True:
        try:
            n = int(input('Digite um número: '))
            lista(n)
            break
            
        except:
            print('Número inválido. Digite Novamente.')



if __name__=='__main__':
    main()

            

            
