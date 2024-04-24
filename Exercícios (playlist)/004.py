import os

os.system("cls||clear")

algo = input('Digite algo: ')

print(type(algo))
print("Só tem espaços?",algo.isspace())
print("É um número?",algo.isnumeric())