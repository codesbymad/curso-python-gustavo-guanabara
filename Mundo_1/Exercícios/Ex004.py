dig = input("Digite qualquer coisa em seu teclado ")
if dig.isnumeric() :
    print("Você digitou numeros")
elif(dig.isalnum()):
    print("Você digitou letras e numeros")
elif(dig.isalpha):
    print("Você digitou letras")
else:
    print("Você não digitou nada")