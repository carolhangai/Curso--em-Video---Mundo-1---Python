#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual salario do funcionario: R$'))
aumento = sal * (15/100)
novo_sal = aumento + sal
print('O Funcionario que recebia R${}, passa a receber o salario com 15% de aumento R${:.2f}'. format(sal,novo_sal))
print('O aumento de 15% equivale a R${}'. format(aumento))
