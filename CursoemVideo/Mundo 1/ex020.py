#  o mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que
#  leia o nome dos quatro alunos e mostre na tela a ordem sorteada.

from random import shuffle

a = input('Digite o nome do aluno: ')
b = input('Digite o nome do aluno: ')
c = input('Digite o nome do aluno: ')
d = input('Digite o nome do aluno: ')
alunos = [a, b, c, d]
shuffle(alunos)

print('Ordem de apresentação dos trabalhos:\n')
print('1 - {}\n2 - {}\n3 - {}\n4 - {}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))
