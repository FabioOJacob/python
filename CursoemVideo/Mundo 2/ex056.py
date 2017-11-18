'''desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

- A média de idade do grupo
- qual é o nome do homem mais velho.
- quantas mulheres tem menos de 20 anos.'''

n = []
idd = []
sx = []
contM = 0
h = []
hidd = []
for i in range(4):
    nome = str(input('Digite seu nome: ').capitalize())
    n.append(nome)
    idade = int(input('Digite sua idade: '))
    idd.append(idade)
    sexo = str(input('Seu sexo: (H ou M) ').upper())
    sx.append(sexo)
# verifica quantidade de mulheres abaixo de 20 anos
    if idade < 20 and sexo == 'M':
        contM += 1
        
    if sexo == 'H':
        h.append(nome)
        hidd.append(idade)

# verifica a média de idade do grupo
media = (idd[0] + idd[1] + idd[2] + idd[3]) / 4

# verifica a posição na lista do homem mais velho
idx = hidd.index(max(hidd))
maisVelho = h[idx]

print('\nnome', n)
print('idade', idd)
print('sexo', sx)
print('homens: ', h)
print('idade H: ', hidd)

print('\nA média de idade é {:.1f} anos.'.format(media))
print('O homem mais velho é {}, com {} anos.'.format(maisVelho, hidd[idx]))
print('Mulheres abaixo dos 20 anos: {}'.format(contM))
