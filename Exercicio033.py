""": Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))
v3 = int(input('Digite o terceiro valor:'))

if v1 < v2 and v1 < v3:
    menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
if v1 > v2 and v1 > v3:
    maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print(f'O menor numero digitado foi:',menor)
print(f'O maior numero digitado foi:', maior)



