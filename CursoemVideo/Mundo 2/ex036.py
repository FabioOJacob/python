# Escreva um programa para aprovar o empréstimo bancário para
# comprar uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o emprestimo será negado.

print('*' * 60)
print(str('Empréstimo Bancário.').upper())
print('*' * 60)
print('')
valor = float(input('Qual o valor do imóvel que deseja? '))
salario = float(input('Qual o seu salário bruto? '))
anos = int(input('Em quantos anos você deseja quitar? '))
meses = anos * 12
salario_30 = salario * (30 / 100)
prestacao = valor / meses
print('')

if prestacao > salario_30:
    print('Empréstimo NEGADO')
    print('A prestação do imóvel desejado será de R$ {:.2f}, e é maior que 30% do seu salário.'.format(prestacao))
    print('Tente aumentar o número de parcelas.')
else:
    print('Empréstimo APROVADO!!!')
    print('Valor das prestações: R$ {:.2f}.'.format(prestacao))

print('')
""" print('Custo do Imóvel: R$ {:.2f}'.format(valor))
print('Valor do salário bruto: R$ {:.2f}'.format(salario))
print('meses = {}'.format(meses))
print('30% do salário = {:.2f}'.format(salario_30))
print('Valor das prestações: R$ {:.2f}'.format(prestacao)) """
