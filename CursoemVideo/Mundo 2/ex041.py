# A confedereção de natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre a sua categoria,
# de acordo com a idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
#  Acima: MASTER

from datetime import datetime

now = datetime.now()

anoNasc = int(input('Informe o ano do seu nascimento: '))
idade = now.year - anoNasc

if idade <= 9:
    print('Sua categoria é MIRIM.')
elif 9 < idade <= 14:
    print( 'Sua categoria é INFANTIL.')
elif 14 < idade <= 19:
    print('Sua categoria é JUNIOR.')
elif 19 < idade <= 20:
    print('Sua categoria é SÊNIOR.')
elif idade > 105:
    print('Ano de nascimento inválido.')
else:
    print('Sua categoria é MASTER.')
