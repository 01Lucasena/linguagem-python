import os
os.system("cls||clear")

soma = 0

for i in range(1,4):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota

media = soma / i

print(f"Média: {media}")
if media >= 7:
    print("Aprovado.")
elif media < 7 and media >= 4:
    print("Recuperação.")
else:
    print("Reprovado.")