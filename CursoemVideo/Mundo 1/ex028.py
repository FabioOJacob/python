# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuario tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

r = random.randint(0, 5)
print('Pensei em um número de 0 à 5,\nque número eu pensei? ')
tenta = int(input('Diga o número: '))
if tenta == r:
    print('Parabéns, você acertou!!\n')
else:
    print('Que pena, você perdeu!!\nO número era {}'.format(r))
print('Pressione ENTER para sair.')