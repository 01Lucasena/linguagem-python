import os
os.system("cls||clear")

QUANTIDADE_DE_NOTAS = 3

#criando uma lista
notas = []

#solicitando 3 notas ao usuário
for i in range(QUANTIDADE_DE_NOTAS):
    
    i += 1
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / QUANTIDADE_DE_NOTAS

i = 0

#exibindo 3 notas e a média aritimética ao usuário
for nota in notas:

    i += 1
    print(f"\n{i}ª Nota: {nota}")

print(f"\nMédia: {media}")