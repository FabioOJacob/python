'''desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 
10 primeiros termos dessa progressão.'''

print('{:=^60}\n'.format(' PROGRESSÃO ARITMÉTICA '))

a = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
print('')
an = 0
n = 10  # número de termos
for i in range(1, n+1):
    an = a + (i - 1) * r
    print(an)