# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
# da passagem, cobrando, R$ 0,50 por Km para viagens de até 200Km e R$ 0,45
# para viagens mais longas.

km = float(input('Qual a distância da viagem, em Km: '))
if km <= 200:
    valor1 = km * 0.50
    print('O custo da passagem é de R$ {:.2f}.'.format(valor1))
else:
    valor2 = km * 0.45
    print('O custo da passagem é de R$ {:.2f}.'.format(valor2))
