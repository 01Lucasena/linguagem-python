import os
os.system("cls||clear")

idade = int(input("Digite sua idade: "))

if idade > 65 or idade < 18:
    print("\nNão é obrigado(a) a votar.")

else:
    print("\nÉ obrigado a votar.")