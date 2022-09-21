# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite uma distancia em metros:'))
km = medida / 1000
hm = medida / 100
dam = medida/ 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('a medida em km é:', km)
print('a medida em hm é:', hm)
print('a medida em dam é:', dam)
print('a medida em dm é:', dm)
print('a medida em cm é:', cm)
print('a medida em mm é:', mm)