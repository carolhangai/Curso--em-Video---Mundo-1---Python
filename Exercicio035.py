"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""
print('-='*20)
print('ANALISADOR DE TRIANGULO...')
print('-='*20)
t1 = float(input('Digite o primeiro segmento:\033[31;33m'))
t2 = float(input('Digite o segundo segmento:'))
t3 = float(input('Digite o terceiro segmento:'))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os segmentos PODEM FORMAR um triangulo!')

else:
    print('Os segmentos NÃO PODEM formar um triangulo!')



