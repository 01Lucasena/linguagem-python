import os

os.system("cls||clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite a 1ª nota: "))
segundaNota = float(input("Digite a 2ª nota: "))
terceiraNota = float(input("Digite a 3ª nota: "))

soma = primeiraNota + segundaNota + terceiraNota
media = soma / 3

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Média: {media}")

if media > 7:
    print("\nAprovado.")
else:
    print("\nReprovado.")