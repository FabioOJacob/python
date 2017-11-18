'''refaça o desafio 09, mostrando tabuada de um numero que o usuario escolher, so que
agora utilizando um laço for'''


n = int(input('Digite um número para ver a sua tabuada: '))
print('*' * 12)
print('{}{}'.format('TABUADA DO ', n))
print('*' * 12)
print('\n')
for i in range(0, 11):
    print('{} x {:2} = {:2}'.format(n, i, n * i))
print('\nFIM')
