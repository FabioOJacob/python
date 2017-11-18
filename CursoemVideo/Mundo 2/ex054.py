'''Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
maiores. (21 anos maioridade)'''

from datetime import date

menor = 0
maior = 0
hoje = date.today().year
for i in range(7):
    anoNasc = int(input('Digite o ano que você nasceu: '))
    idade = hoje - anoNasc
    if idade < 21:
        menor += 1
        print('Você tem {} anos.'.format(idade))
    else:
        maior += 1
        print('Você tem {} anos.'.format(idade))
print('Temos {} pessoas menores de 21 anos e {} pessoas maoires de 21 anos.'.format(menor, maior))

