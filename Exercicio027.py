# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Qual é seu nome?')).strip()
name = nome.split()
print(name)
print('Muito prazer em conhece-lo!\033[4;30;41m')
print('Seu primeiro nome é {}\033[1;32m'.format(name[0]))
print('Seu ultimonome é {}.'.format(name[len(name)-1]))