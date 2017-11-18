# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

f = str(input('Escreva uma frase: ')).lower().strip()
#  print('quantidade de letras: ', len(f))
print('A contagem de "A" é: {}'.format(f.count('a')))
print('A posição do primeiro "A" é: Posição {}'.format(f.find('a')))
last = f[::-1].find('a')
print('A posição do último "A" é: Posição {}'.format((len(f) - 1) - last))
