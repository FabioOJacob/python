# Crie um programa que faça o computador jogar jokenpô com vc.

import random
import time


print('=' * 30)
print('{:^30}'.format('JO-KEN-PÔ'))
print('=' * 30)
print('')

escolha = random.randint(1, 3)

joken = ['Pedra', 'Papel', 'Tesoura']
print('''Escolha uma opção:
[1] Pedra
[2] Papel
[3] Tesoura''')

user = int(input())

# verifica o que o computador escolheu
if escolha == 1:
    compEscolhe = joken[0]
elif escolha == 2:
    compEscolhe = joken[1]
else:
    compEscolhe = joken[2]

#  verifica o que o usuário escolheu
if user == 1:
    userEscolhe = joken[0]
elif user == 2:
    userEscolhe = joken[1]
elif user == 3:
    userEscolhe = joken[2]

print('')
print('Jo')
time.sleep(1)
print('ken')
time.sleep(1)
print('pô')

print('')
print('Computador:', compEscolhe)
print('Você:', userEscolhe)
print('')

# verifica quem ganhou.
# Pedra ganha de Tesoura, mas perde de Papel
# Tesoura ganha de Papel, mas perde de Pedra
# Papel ganha de Pedra, mas perde de Tesoura

if user == 1 and escolha == 3:
    print('Você GANHOU!!!')
elif user == 1 and escolha == 2:
    print('Você PERDEU!!!')
elif user == 3 and escolha == 2:
    print('Você GANHOU!!!')
elif user == 3 and escolha == 1:
    print('Você PERDEU!!!')
elif user == 2 and escolha == 1:
    print('Você GANHOU!!!')
elif user == 2 and escolha == 3:
    print('Você PERDEU!!!')
elif user == escolha:
    print('EMPATE.')


