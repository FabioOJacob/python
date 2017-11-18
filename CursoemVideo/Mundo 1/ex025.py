# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Informe o nome completo: ')).lower().split()
print('o nome digitado contem "silva": {}'.format('silva' in nome))

