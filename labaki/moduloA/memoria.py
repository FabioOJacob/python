import random

r = random.random
print('\n' * 3)
print('''memória \n
não jogue usando o IDLE
digite todos os numeros que forem
informados pelo computador.''')
print('\n' * 4)
escolha = int(10*r())
print('Meu número:', escolha)
a = str(escolha)
user = str(int(input('Sua vez, tente: ')))
print('\n' * 20)
while user == a:
    escolha = int(10 * r())
    print('Meu número:', escolha)
    a = a + str(escolha)
    user = str(int(input('Sua vez, tente:')))
    print('\n' * 20)
print('Você perdeu!!!')
print('Seu saldo:', len(a))