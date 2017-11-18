#  Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse ângulo

from math import cos, sin, tan, radians

print('Digite um ângulo qualquer: ')
ang = float(input())
angr = radians(ang)  # convertendo o ângulo para radianos
cos = cos(angr)
sen = sin(angr)
tg = tan(angr)
print('Para o ângulo {}°, temos: \nSeno = {:.3f}\nCosseno = {:.3f}\nTangente = {:.3f}'.format(ang, sen, cos, tg))
