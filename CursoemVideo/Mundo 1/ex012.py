#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

p = float(input('Insira o valor do produto: R$ '))
d = float(0.05) # valor que será utilizado para dar o desconto.
pd = (p - (p * d))
print('O valor do produto com {}% de desconto é R$ {:.2f}.'.format(int(d*100), pd))