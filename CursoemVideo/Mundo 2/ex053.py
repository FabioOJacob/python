'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços.
ex.:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA BOLO
ANOTARAM A DATA DA MARATONA'''

texto = str(input('Digite uma frase: ')).strip()
print(texto)
for i in texto:

    print(i)