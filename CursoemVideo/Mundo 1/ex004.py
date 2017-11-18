#DESAFIO 04 - faça um programa que leia algo pelo teclado e mostre na tela o seu tipo PRIMITIVO e todas
#as informações possiveis sobre ele.
n = input('Digite qualquer coisa aqui: ')
print(type(n))
print('O que foi digitado é um número? ', n.isnumeric())