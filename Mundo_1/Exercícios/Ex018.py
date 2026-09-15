# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = int(input("Digite um angulo (de 0 a 360°): "))
rad = math.radians(ang)
cos = math.cos(rad)
sen = math.sin(rad)
tan = math.tan(rad)
print(f"NO angulo de {ang}°, o cosseno é {cos:.2f}, o seno é {sen:.2f} e a tangente é {tan:.2f}")