import os

#função sem retorno.
def logoSenai():
    os.system("cls||clear")
    print("\t===========")
    print("\t===SENAI===")
    print("\t===========\n")

#função para calculo de inflação
def inflacao(preco):
    
    if preco >= 100:
        
        desconto = preco * 0.2
        inflacao = preco + desconto
        print(f"Preço com inflação: {inflacao}")
    
    else:

        desconto = preco * 0.1
        inflacao = preco + desconto
        print(f"Preço com inflação: {inflacao}")

#solicitando dados
logoSenai()
preco = float(input("Digite o preço do produto: R$"))

#imprimindo dados
logoSenai()
inflacao(preco)