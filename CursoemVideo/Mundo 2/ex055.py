'''Faça um programa que leia o peso de cinco pessoas. No final, mostre
qual foi o maior e o menor peso lido.'''

p = []
for i in range(5):
    peso = float(input('Digite seu peso: '))
    p.append(peso)
print('O maior peso digitado foi {:.2f} Kg e o menor peso foi {:.2f} Kg.'.format(max(p), min(p)))
