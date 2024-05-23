import os
os.system("cls||clear")

#Criando uma lista

notas = []

#Solicitando 3 notas ao usuário
for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota) 

#Exibindo as notas para o usuário
for i in range(3):
    print(f"Nota: {notas[i]}")