#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta em Fahrenheit.

c = float(input('Entre com a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {:.2f}ºC equivale a {:.2f}ºF.'.format(c, f))
