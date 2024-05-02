import os
os.system("cls||clear")

numero = int(input("Digite um número: "))

for i in range (1,11):
    produto = i * numero 
    print(f"{i} x {numero}: {produto}")