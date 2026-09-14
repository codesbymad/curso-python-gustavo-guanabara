# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input("Digite a largura da parede: "))
a = float(input("Digite a altura da parede: "))
area = a*l
qTinta = area/2
print(f"A área da parede é {area} e a quantidade de tinta necessária para pinta-la é {qTinta}")