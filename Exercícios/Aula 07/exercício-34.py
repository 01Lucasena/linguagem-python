import os

#função sem retorno.
def logoSenai():
    
    os.system("cls||clear")
    print("\t===========")
    print("\t===SENAI===")
    print("\t===========\n")
    
#solicitando dados ao usuário.
logoSenai()
nome = input("Digite seu nome: ")

logoSenai()
idade = int(input("Digite sua idade: "))

logoSenai()
peso = float(input("Digite seu peso: "))

#exibindo dados ao usuário
logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")