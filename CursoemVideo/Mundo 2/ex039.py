# Faça um programa que leia o ano de nascimento de um jovem e
# informe, de acordo com a sua idade:

# Se ele ainda vai se alista so serviço militar;
# Se é a hora de se alistar;
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que
# passou do prazo.

from datetime import datetime

now = datetime.now()
anoNasc = int(input('Digite o ano do seu nascimento: '))
idade = now.year - anoNasc

if idade < 17:
    print('Você ainda é muito novo para se alistar.')
elif 17 <= idade <= 18:
    print('Já está na hora de se alistar.')
else:
    print('Você já passou da idade de se alistar.')
