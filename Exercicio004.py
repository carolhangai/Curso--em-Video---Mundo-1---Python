# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

a = input('Digite algo:')
print('O tipo primitivo desse valo é:', type(a))
print('Só tem espacos?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Esta em maiusculas?', a.isupper())
print('Esta em minuscula:', a.islower())
print('Esta capitalizada?', a.istitle())


