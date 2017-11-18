# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em Maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('O seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
primeiro = nome.split()
print('O primeiro nome é {} e tem {} letras.'.format(primeiro[0], len(primeiro[0])))
# outra forma de contar o primeiro nome: usando find para encontrar o primeiro espaço
# print('O primeiro nome é {} e tem {} letras.'.format(nome, nome.find(' ')))