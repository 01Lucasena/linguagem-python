import os
os.system("cls||clear")

pares = 0
impares = 0 

for i in range(1,6):
    numero = int(input(f"Digite o {i}º número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de numeros pares: {pares}")
print(f"Quantidade de numeros ímpares: {impares}")