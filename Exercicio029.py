"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""

vel = float(input('Qual a velocidade atual do carro:'))
print('A velocidade permitida na via é de 80 KM')
vel_per = vel - 80
multa = 7 * vel_per
if vel > 80:
    print('Voce foi multado em R$',multa, 'reais','.' 'Sua velocidade foi de {} km'.format(vel))
else:
    print('Tenha um Bom Dia! Sua velocidade foi {}Km'.format(vel))