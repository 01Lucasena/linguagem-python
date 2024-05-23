import os
os.system ("cls||clear")

QUANTIDADE_DE_NUMEROS = 5
numeros = []

#solicitando 5 numeros ao usuário
for i in range(QUANTIDADE_DE_NUMEROS):
    
    i += 1
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)

i = 0
print("\n")
#exibindo dados ao usuário

for i, numero in enumerate(numeros):
    
    print(f"{i+1}º Número: {numero}")

print(f"\nMaior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")