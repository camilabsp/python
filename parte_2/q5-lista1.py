'''Você está fazendo uma reforma em casa e precisa calcular a quantidade de piso para sua sala e a quantidade de tinta a ser usada 
nas paredes. Precisa também saber qual o volume da sala em metros cúbicos para estimar a potência necessária para o ar 
condicionado. Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e largura 
da sala em metros e em seguida imprima: area do piso da sala, volume da sala e area das paredes da sala.'''

def area_piso(c,l):

    area = l * c

    return area

def volume_sala(a,c,l):

    volume = l * c * a

    return volume

def area_parede(a,c,l):

    area_p = (2 * a * l) + (2 * a * c)

    return area_p


def main():

    a = float(input('Digite o valor da área (em metros): '))
    c = float(input('Digite o valor do comprimento (em metros): '))
    l = float(input('Digite o valor da largura (em metros): '))

    print(f'Área do piso da sala: {area_piso(c,l):.2f} m²\nVolume da sala: {volume_sala(a,c,l):.2f} m³\nÁrea das paredes da sala: {area_parede(a,c,l):.2f} m²')


if __name__=='__main__':
    main()
