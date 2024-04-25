import os

os.system("cls||clear")

primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))

soma = primeiraNota + segundaNota
media = soma / 2

print(f"\nPrimeira nota: {primeiraNota}")
print(f"\nSegunda nota: {segundaNota}")
print(f"\nMédia: {media}")

if media > 7:
    print("\nAprovado.")

elif media < 7 and media >= 5:
    print("\nRecuperação.")

else:
    print("\nReprovado.") 