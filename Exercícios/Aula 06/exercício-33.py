import os
os.system("cls||clear")

QUANTIDADE_DE_NUMEROS = 6
contadorPares = 0
contadorInpares = 0
numeros = []

#solicitando números ao usuário

for i in range(QUANTIDADE_DE_NUMEROS):

    numero = int(input(f"Digite o {i+1}º número: "))

    if numero %2 == 0:

        contadorPares += 1
    
    else:

        contadorInpares += 1

    numeros.append(numero)

print("\n")

#exibindo dados ao usuário

for i, numero in enumerate(numeros):

    print(f"{i+1}º Número: {numero}")
    
print(f"\nQuantidade de números pares: {contadorPares}")
print(f"Quantidade de números ínpares: {contadorInpares}")