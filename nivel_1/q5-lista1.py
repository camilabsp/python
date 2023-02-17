'''No próximo final de semana seu time de futebol entrará em campo. Escreva um programa que leia o seu nível de 
empolgação para a partida, um número inteiro entre 1 e 10, e mostre a empolgação do lado de fora do estádio
representando por letras “O” ao gritar GOL.'''

n = int(input('Qual é o seu nível de empolgação para o jogo (1 a 10)? '))

gol = 'G' + ('o' * n) + 'l!'

print(f'Empolgação nível {n} >>> {gol}')
