# Desenvolva uma lógica que leia o peso e a altura de uma
# pessoa, calcule o seu IMC e mostre seu status, de acordo
# com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Qual seu peso: '))
alt = float(input('Qual sua altura: '))
imc = peso / (alt * alt)
print('Seu IMC é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está OBESO(A).')
else:
    print('CUIDADO você está com OBESIDADE MÓRBIDA.')