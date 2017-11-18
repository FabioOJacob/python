# Escreva um programa que leia dois números inteiros e
# compare-os, mostrando na tela uma mensagem:

# - O primeiro valor é maior;
# - O segundo valor é maior;
# - Não existe valor maior, os dois são iguais.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro: '))

if num1 > num2:
    print('O primeiro número digitado é maior que o segundo.')
elif num2 > num1:
    print('O segundo número digitado é maior que o primeiro.')
else:
    print('Os dois números são iguais.')