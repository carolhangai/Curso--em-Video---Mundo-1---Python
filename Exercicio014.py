#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Qual temperatura em Celsius:'))
far = ((9*cel)/5) + 32
print('A temperatura de {}º C, em Farenheit equivale a {}ºF'.format(cel,far))