# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. US$1.00 ==  R$5.14

real = float(input("Quantos reais você tem? "))
dolar = real/5.14
print(f"Com R${real}, você consegue comprar US${dolar:.2f}")