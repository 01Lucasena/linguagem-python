import os

#função sem retorno.
def logoSenai():
    
    os.system("cls||clear")
    print("\t===========")
    print("\t===SENAI===")
    print("\t===========\n")

QUANTIDADE_DE_NUMEROS = 10

#função tabuada
def exibirTabuada(numero):
    for i in range(QUANTIDADE_DE_NUMEROS):
        print(f"{numero} x {i+1} = {numero * (i+1)}")

#solicitar dados ao usuário
logoSenai()
numero = int(input("Digite um número: "))

#imprimir resultado
logoSenai()
print(f"=== TABUADA DO {numero} ===")
exibirTabuada(numero)