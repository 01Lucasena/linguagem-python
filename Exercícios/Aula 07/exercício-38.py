import os

#função sem retorno.
def logoSenai():
    os.system("cls||clear")
    print("\t===========")
    print("\t===SENAI===")
    print("\t===========\n")

#função para contagem de números pares
def contagemPares(numero):
    pares = 0
    for numero in numeros:
        if numero %2 == 0:
            pares += 1

    print(f"Quantidade de números pares: {pares}")

#função para contagem de números impares
def contagemImpares(numero):
    impares = 0
    for numero in numeros:
        if numero %2 != 0:
            impares += 1

    print(f"Quantidade de números ímpares: {impares}")     

QUANTIDADE_DE_NUMEROS = 6
numeros = []

#solicitando dados.
logoSenai()
for i in range(QUANTIDADE_DE_NUMEROS):
    i += 1
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)

#imprimindo dados
logoSenai()
contagemPares(numero)
contagemImpares(numero)