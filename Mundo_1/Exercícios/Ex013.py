# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input("Qual o seu salário atual? "))
sN = s + (s * 15/100)
print(f"O novo valor do seu salário sera R${sN}")