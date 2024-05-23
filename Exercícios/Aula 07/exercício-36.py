import os

#função sem retorno.
def logoSenai():
    
    os.system("cls||clear")
    print("\t===========")
    print("\t===SENAI===")
    print("\t===========\n")

#função para cálculo de média aritimética
def calcularMedia(n1,n2):
    return (n1 + n2) / 2

#solicitando dados ao usuário.
logoSenai()
primeiroNumero = float(input("Digite o 1º número: "))
segundoNumero = float(input("Digite o 2º número: "))

#exibindo dados ao usuário
logoSenai()
print(f"1º Número: {primeiroNumero}")
print(f"2º Número: {segundoNumero}")
print(f"Média: {calcularMedia(primeiroNumero,segundoNumero)}")