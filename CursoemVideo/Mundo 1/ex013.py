#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input('Digite o salário aqui: '))
a = float(0.15) # valor para calcular o aumento de salário
sa = float(s + (s * a))
print('Seu novo salário com {}% de aumento será R$ {}.'.format(int(a * 100), sa))
