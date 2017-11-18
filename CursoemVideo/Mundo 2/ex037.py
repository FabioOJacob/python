# Escreva um programa que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão.

# 1- para binário
# 2- para octal
# 3- para hexadecimal

num = int(input('Digite um numero: '))
print('Para qual base você deseja converter:')
print('1- BINÁRIO \n2- OCTAL \n3-HEXADECIMAL')
base = int(input())
Bin = format(num, 'b')
Oct = format(num, 'o')
Hex = format(num, 'X')
if base == 1:
    print('{} em Binário é {}.'.format(num, Bin))
elif base == 2:
    print('{} em Octal é {}.'.format(num, Oct))
else:
    print('{} em Hexadecimal é {}.'.format(num, Hex))
