# Crie um programa que leia se um número é par ou impar.

n = int(input('Digite um número qualquer: '))
if n % 2 == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))
