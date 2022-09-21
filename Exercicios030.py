"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR"""

num = int(input('Digite um numero:'))
print('Numero escolhido foi:{}'.format(num))
if num % 2 == 0:
    print('{} é um numero PAR'. format(num))
else:
    print('{} é um numero IMPAR'.format(num))
