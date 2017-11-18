import math

num = int(input('Digite um Número: '))
raiz = math.sqrt(num)
print('A raiz de {} é {}'.format(num, raiz))
print('A raiz de {} é {}'.format(num, math.ceil(raiz)))  # ceil = arredondamento para cima
print('A raiz de {} é {}'.format(num, math.floor(raiz)))  # floor = arredondamento para baixo
print('A raiz de {} com valor truncado é {}'.format(num, math.trunc(raiz)))  # trunc = truncamento
