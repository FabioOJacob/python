# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de
# pagamento:

# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão de crédito: 5% de desconto
# em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Qual o valor do produto: R$ '))
print('Escolha a forma de pagamento:') 
print('[1] a vista em dinheiro ou cheque.')
print('[2] a vista no cartão de crédito')
print('[3] em 2x no cartão')
print('[4] em 3x ou mais no cartão')
pag = int(input())
if pag == 1:
    custo = valor - (valor * (10 / 100))
    print('Para pagamento a vista, você terá um desconto de 10%. O valor a ser pago é de R$ {:.2f}.'.format(custo))
elif pag == 2:
    custo = valor - (valor * (5 / 100))
    print('Para pagamento a vista no cartão, você terá desconto de 5%. O valor a ser pago é de R$ {:.2f}.'.format(custo))
elif pag == 3:
    print('Para pagamento em 2 vezes, o valor é de R$ {:.2f}.'.format(valor))
elif pag == 4:
    custo = valor + (valor * (20 / 100))
    print('Para pagamento em 3 ou mais vezes, haverá um acréscimo de 20%. O valor a ser pago é de R$ {:.2f}.'.format(custo))
