# Desenvolva um programa que leia o comprimento de três retas e ao usuário se eles podem ou não formar um triângulo.

a = int(input('Digite a distancia do primeiro lado: '))
b = int(input('Digite a distancia do segundo lado: '))
c = int(input('Digite a distancia do terceiro lado: '))
if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('As retas a = {}, b = {} e c = {}, podem formar um triangulo.'.format(a, b, c))
else:
    print('As retas a = {}, b = {} e c = {}, não podem formar um triangulo.'.format(a, b, c))
