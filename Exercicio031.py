"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

"""viagem = float(input('Qual a distancia de sua viagem?'))
print('Voce esta prestes a comecar uma viagem de {}KM'.format(viagem))
pass_duz = viagem * 0.50
pass_lon = viagem * 0.45
if viagem <= 200:
    print('O preco de sua viagem será de R${}'.format(pass_duz))
else:
    print('O preço de sua viagem custará R${}'.format(pass_lon))
print('BOA VIAGEM!')"""

distancia = float(input('Qual é a distancia e sua viagem?'))
print('Voce esta prestes a comecar uma viagem de {} KM'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço de sua passagem será de R${}'.format(preco))
