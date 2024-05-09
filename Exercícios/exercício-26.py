import os
os.system("cls||clear")

soma = 0
i = 0

while True:

    numero = int(input("Digite um número: "))

    if numero > 0:
        i += 1
        soma += numero

    else:
        media = soma / i
        print(f"Média: {media}")
        break