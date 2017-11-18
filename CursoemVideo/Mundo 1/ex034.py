# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# para salários superiores a R$ 1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário: '))
if salario > 1250.0:
    aumento = salario + (salario * 0.1)
    print('Você terá um aumento de 10% e receberá R$ {:.2f} a mais, totalizando R$ {:.2f}.'.format(salario * 0.1, aumento))
else:
    aumento = salario + (salario * 0.15)
    print('Você terá um aumento de 15% e receberáR$ {:.2f} a mais, totalizando R$ {:.2f}.'.format(salario * 0.15, aumento))
