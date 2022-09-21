#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa

#co = float(input('Comprimento cateto oposto:'))
#ca = float(input('Comprimento cateto adjacente:'))
#hip = (co **2+ ca**2) **(1/2)
#print('A hipotenusa mede {:.2f}'.format(hip))

import math
co = float(input('Comprimento cateto oposto:'))
ca = float(input('Comprimento cateto adjacente:'))
hip = math.hypot(co,ca)
print('A hipotenusa mede {:.2f}'.format(hip))