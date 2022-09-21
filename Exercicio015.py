#Escreva um programa que pergunte a quantidade de Km percorridos  por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quilometragem percorrida: '))
dias = float(input('Quantos dias de uso do carro:'))
diaria = 60
preco_km = 0.15
pagar = (dias * diaria) + (km*preco_km)
print('O Valor da pagar por {} dias de uso, percorrendo um total de {}KM, é de R${:.2f} reais'. format(dias, km, pagar))


