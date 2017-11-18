# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Informe uma cidade: '))
p = cidade.lower().split()
print('Esta cidade começa com "santo": {}'.format(p[0].lower() == 'santo'))