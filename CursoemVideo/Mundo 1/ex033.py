# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n2 < n1 > n3:
    print('{} é maior que {} e {}.'.format(n1, n2, n3))
elif n1 < n2 > n3:
    print('{} é maior que {} e {}.'.format(n2, n1, n3))
else:
    print('{} é maior que {} e {}.'.format(n3, n1, n2))
