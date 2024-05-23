import os

#função sem retorno.
def logoSenai():
    
    os.system("cls||clear")
    print("\t===========")
    print("\t===SENAI===")
    print("\t===========\n")

#funções para cálculo de variáveis
def somar(n1,n2):
    return n1 + n2
def subtrair(n1,n2):
    return n1 - n2
def multiplicar(n1,n2):
    return n1 * n2
def dividir (n1,n2):
    return n1/n2
   
#solicitando dados ao usuário
logoSenai()
primeiroNumero = float(input("Digite o 1º número: "))
segundoNumero = float(input("Digite o 2º número: "))
   
logoSenai()
print(f"Soma: {somar(primeiroNumero,segundoNumero)}")
print(f"Subtração: {subtrair(primeiroNumero,segundoNumero)}")
print(f"Multiplicação: {multiplicar(primeiroNumero,segundoNumero)}")
print(f"Divisão: {dividir(primeiroNumero,segundoNumero)}")