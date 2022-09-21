"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""

"""sal = float(input('Qual salario do funcionario?'))
if sal > 1250:
    aumento = (sal*0.10)
    print('Quem ganhava R$',sal, 'passa a ganhar R$',aumento + sal, 'agora.')
if sal <= 1250:
    aumento = (sal*0.15)
    print('Quem gannhava R$', sal, 'passa a ganhar R$', aumento + sal, 'agora.')"""

sal = float(input('Qual salario do funcionario?'))
if sal <=1250:
    aumento = (sal + 1250 *15/100)
else:
    aumento = (sal + 1250 * 10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, aumento))