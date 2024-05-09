import os
os.system("cls||clear")

i = 1
soma = 0

while True:

    nota = float(input("Digite uma nota: "))
    opcao = input("Deseja inserir uma nota? (Digite 'S' para sim ou 'N' para não.) ")
    
    opcao = opcao.upper()

    if opcao != "N":
        
        soma += nota
        i += 1

    else:
        break

media = soma / i

if i == 1:
    media = nota

print(f"Média: {media}")
print(f"Nº de repetições: {i}")
