# Escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80Km/h, mostre na tela uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

from termcolor import colored, cprint

vel = int(input('Diga qual a velocidade do carro: '))

if vel <= 80:
    print('Você está dentro do limite de velocidade!')
    cprint('Parabéns, continue obedecendo as Leis de Trânsito!', 'red', 'on_yellow')
else:
    multa = (vel - 80) * 7.0
    cprint('Você ultrapassou a velocidade permitida de 80Km/h em {}Km/h.'.format(str(vel - 80)), 'yellow')
    cprint('Levou uma multa de R$ {:.2f}.'.format(multa), 'red')
input('tecle enter')
