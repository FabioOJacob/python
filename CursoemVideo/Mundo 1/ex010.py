#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ele pode comprar
# US$ 1,00 = R$ 3,27

r = float(input('Quanto, em reais, você deseja converter? '))
us = (r*3.27)
print('R$ {:.2f} reais pode comprar US$ {:.2f} em dólares'.format(r, us))
