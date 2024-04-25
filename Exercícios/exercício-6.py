import os
os.system("cls||clear")

loginCadastrado = "usuario123"
senhaCadastrada = "123456"

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == loginCadastrado and senha == senhaCadastrada:
    print(f"\nBem-Vindo!")

else:
    print("\nLogin ou senha inválidos.")