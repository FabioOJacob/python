#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
#  o nome deles e escrevendo o nome escolhido.

import random

alunos = []
alunos.append(input('Digite o nome do primeiro aluno: '))
alunos.append(input('Digite o nome do segundo aluno: '))
alunos.append(input('Digite o nome do terceiro aluno: '))
alunos.append(input('Digite o nome do quarto aluno: '))

escolhido = random.randint(1, 5)
print('O escolhido para apagar o quadro foi {}.'.format(alunos[escolhido]))
