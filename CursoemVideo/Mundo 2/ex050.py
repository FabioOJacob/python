'''desenvolva um programa que leia seis numeros inteiros e mostra a soma apenas daqueles que
forem pares. Se o valor digitado for impar, desconsidere-o'''

s = 0
for i in range(6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
if s == 0:
    print('\nVocê não digitou nenhum número PAR!!!')
else:
    print('\nA somatória dos números PARES digitados é {}.'.format(s))
