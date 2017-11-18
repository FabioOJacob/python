#Faça um programa que leia altura e largura de uma parede em metros, calcule a sua área e a quentidade de
#tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

t = float(2)  # quantidade de metros quadrados que 1 litro de tinta pinta
a = float(input('Qual a altura da parede, em m²? '))
l = float(input('qual a largura da parede, em m²? '))
ar = float(a * l)
print('Área total da parede, {:.2f} m².'.format(ar))
print('Você precisará de {:.2f} litros de tinta para pintar esta parede.'.format(ar * t))
