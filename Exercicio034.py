"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""

sal = float(input('Qual o seu salario?:'))
if sal > 1250:
    print(sal)*0.10
    