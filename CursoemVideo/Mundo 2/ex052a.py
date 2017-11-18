"""Faça um programa que leia um numero inteiro e diga se ele é primo ou não."""

tot = 0
n = int(input('Digite um número: '))
for i in range(1, n + 1):
    
    if n % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('é PRIMO')
else:
    print('não é PRIMO')
