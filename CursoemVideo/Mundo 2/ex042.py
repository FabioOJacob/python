# Refaça o ex035 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isóceles: dois lados iguais
# - Escaleno: todos os lados diferentes.

# Desenvolva um programa que leia o comprimento de três retas e ao usuário se eles podem ou não formar um triângulo.

a = int(input('Digite a distancia do primeiro lado: '))
b = int(input('Digite a distancia do segundo lado: '))
c = int(input('Digite a distancia do terceiro lado: '))
if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('As retas a = {}, b = {} e c = {}, podem formar um triangulo.'.format(a, b, c))
    if a == b == c:
        print('E formam um triângulo EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('E formam um triângulo ISÓCELES.')
    elif a != b != c:
        print('E formam um triângulo ESCALENO.')
else:
    print('As retas a = {}, b = {} e c = {}, não podem formar um triangulo.'.format(a, b, c))
