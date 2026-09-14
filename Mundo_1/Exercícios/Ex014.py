#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input("Digite a temperatura em graus Celsius: "))
f = c * (9/5) + 32
print(f"{c}C° em Fahrenheit equivale a {f:.2f}F°")