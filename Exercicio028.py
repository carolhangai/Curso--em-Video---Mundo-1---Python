"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

import random
num = int(input('De 0 a 5 tente adivinhar o numero que o cumputador sorteou:'))
print('Voce digitou o numero:', num)
computador = random.randint(0,5) # computador vai sortear de 0 a 5.
print('PROCESSANDO...')
print('O numero sorteado pelo computador foi:',computador)
if (num == computador):
    print('Parabens! Voce me venceu!')
else:
    print('Tente outra vez! Voce perdeu!')


