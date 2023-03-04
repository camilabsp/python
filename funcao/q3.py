"LISTA 1 - Q3"

def temperatura(t):

    c = ((t - 32)/9)*5

    return c

def main():
    
    while True:
        try:
            t = float(input('Digite a temperatura em graus Fahrenheit: '))
            print(f' A temperatura equivale a {temperatura(t):.2f}°C.')
        except:
            print('Temperatura inválida. Tente Novamente!')
    

if __name__=='__main__':
    main()
