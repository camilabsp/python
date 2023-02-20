'''A Bate Ponto LTDA bonifica seus funcionários de acordo o tempo de serviço na empresa Escreva um programa 
que leia o tempo de serviço de um funcionário e o valor do bônus por ano trabalhado. Mostre na tela quanto será a 
bonificação do funcionário.'''

def bonificacao(t,b):

    saldo = t * b

    return saldo


def main():

    t = int(input('Digite o seu tempo de serviço(em anos): '))
    b = float(input('Digite o valor do bônus anual: '))

    print(f'O valor da sa bonificação será de R$ {bonificacao(t,b):.2f}')


if __name__=='__main__':
    main()
