import os
os.system("cls||clear")

soma = 0

for i in range(1,5):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota

media = soma / i

print(f"Média: {media}")