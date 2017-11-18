#  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#  Calcule e mostre o comprimento da hipotenusa

import math
cop = float(input('Digite o comprimento para o cateto oposto: '))
cad = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(cop, cad)
print('O comprimento da Hipotenusa é {:.2f}.'.format(hi))

