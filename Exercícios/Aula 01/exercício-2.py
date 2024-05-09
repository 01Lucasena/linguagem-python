import os
os.system("cls||clear")

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))

print(f"\nNome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {primeiraNota}")
print(f"Segunda nota: {segundaNota}")
print(f"Média: {(primeiraNota + segundaNota) / 2}")
