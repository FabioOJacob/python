#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por
#dia e R$ 0,15 por KM rodade.

dias = int(input('Por quantos dia você ficou com o carro? '))
km = float(input('Digite quantos Km foi rodado: '))
diaria = 60.00
kilometragem = 0.15
porDia = diaria * dias
porKm = kilometragem * km
total = porDia + porKm
print()
print('Valor a ser pago por ter alugado o carro por {} dia(s) é de R$ {:.2f}.'.format(dias, porDia))
print('Valor a ser pago por rodar {} Km é de R$ {:.2f}.\n'.format(km, porKm))
print('*' * 50)
print('O valor total a ser pago é de R$ {:.2f}'.format(total))
print('*' * 50)
