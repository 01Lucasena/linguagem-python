import os
os.system("cls||clear")

numeros = []


#solicitando dados ao usuário

while True:

    numero = int(input(f"Digite um número: "))

    if numero == 0:

        break

    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)

print("\n")

#exibindo dados ao usuário

for i, numero in enumerate(numeros):

    print(f"{i+1}º Número: {numero}")

print(f"\nMaior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")