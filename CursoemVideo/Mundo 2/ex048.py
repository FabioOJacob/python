'''faça um programa que calcule a soma entre todos os numeros impares que são multiplos de
tres e que se encontram no intervalo de 1 até 500'''

s = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        s += i
        # print(i)
print('A soma dos números de 1 à 500 é {:,}.'.format(s))
