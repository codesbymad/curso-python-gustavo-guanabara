# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmP = float(input("Qual a quantidade de kms percorridos pelo carro que você alugou? "))
qtD = float(input("Qual a quantidade de dias pelos quais ele foi alugado? "))
preco = (60*qtD) + (0.15*kmP)
print(f"O preço pago por {kmP}kms percorridos mais {qtD} dias é R${preco:.2f}")