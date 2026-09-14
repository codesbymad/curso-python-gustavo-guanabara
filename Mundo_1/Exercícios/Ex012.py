# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input("Digite o valor do produto: "))
pN = p - (p * 5/100)
print(f"O novo valor com desconto de 5% será {pN}")