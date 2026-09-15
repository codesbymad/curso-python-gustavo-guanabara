# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
cat_op = float(input("Digite o comprimento do cateto oposto: "))
cat_ad = float(input("Digite o comprimento do cateto adjacente: "))
hip = math.hypot(cat_op, cat_ad)
print(f"Em um triângulo retângulo com o cateto oposto de {cat_op} e o cateto adjascente de {cat_ad}, a hipotenusa será {hip:.2f}")