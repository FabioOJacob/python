#Desenvolva um programa que leia 2 notas de um aluno, calcule e mostre a sua média.

print('notas e médias')
nome = input('Qual o nome do Aluno? ')
n1 = float(input('Qual a primeira nota de {}? '.format(nome)))
n2 = float(input('Qual a segunda nota de {} ? '.format(nome)))
m = (n1+n2)/2
print('A média das notas de {} apresentadas, {} e {}, é {:.1f}'.format(nome, n1, n2, m))