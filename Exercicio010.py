#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#{:.2f} dois numeros flutuantes, ou seja, depois da virgula duas casas.

real = float(input('Digite o valor que voce tem em reais: R$'))
dolar = real / 3.27

print('Com RS{:.2f} voce pode comprar US${:.2f}'.format(real, dolar))