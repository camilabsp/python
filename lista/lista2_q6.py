'''6)Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
e quantos faturamentos estão abaixo da média'''

import random
def faturamento():

    quantidade = []
    preco = []
    faturamento = []
    faturamento_total = 0
    abaixo_media = 0

    for i in range(20):
        q = random.randint(1,10)
        p = random.randint(1,50)
        quantidade.append(q)
        preco.append(p)
        fat = preco[i] * quantidade[i]
        faturamento.append(fat)
        
    for fat in faturamento:
        faturamento_total += fat
        media = faturamento_total / 20
        
    for fat in faturamento:
        if fat < media:
            abaixo_media +=1
        else:
            pass
    
    print(f'Quantidade: {quantidade}')
    print(f'Preço: {preco}')
    print(f'Faturamento: {faturamento}')
    print(f'Faturamento Total: {faturamento_total}')
    print(f'Média de Faturamento: {media}')
    print(f'Faturamentos abaixo da média: {abaixo_media}')
   

def main():

    faturamento()

if __name__=='__main__':
    main()
