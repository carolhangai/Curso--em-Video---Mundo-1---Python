#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Digite um numero entre 0 e 9999:'))
u = num//1  % 10
d = num//10 % 10
c = num//100 %10
m = num//1000 %10
print('Analisando o numero {}'. format(num))
print('Unidade:{}',format(u))
print('Dezena:{}',format(d))
print('Centena:{}',format(c))
print('Milhar:{}',format(m))