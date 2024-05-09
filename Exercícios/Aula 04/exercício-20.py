import os
os.system("cls||clear")

while True:
    nota = float(input("Digite uma nota: "))

    if nota < 0 or nota > 10:
        print("\nNota inválida, digite novamente.")
    else:
        print(f"\nNota: {nota}")
        break