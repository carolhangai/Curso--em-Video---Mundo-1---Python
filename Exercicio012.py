# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco =  float(input('Digite o valor do produto: R$'))
novo_preco = preco - (preco * 5 / 100)
print('O produto que custava R${}, na promocao com desconto de 5% vai custar R${}'. format(preco, novo_preco))
print('O desconto foi de R$', preco-novo_preco)