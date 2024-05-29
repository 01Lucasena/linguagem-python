import os

def logoSenai():
    os.system("cls||clear")
    print("\t===========")
    print("\t===SENAI===")
    print("\t===========\n")

while True:

    logoSenai()
    print("\tCALCULADORA\n")
    a = int(input("Digite o 1º número: "))
    b = int(input("Digite o 2º número: "))
    logoSenai()
    operador = input("Digite um sinal operador (+,-,*,/): ")

    match operador:

        case '+':
            logoSenai()
            resultado = a + b
            print(f"\nResultado: {resultado}")
        case '-':
            logoSenai()
            resultado = a - b
            print(f"\nResultado: {resultado}")
           
        case '*':
            logoSenai()
            resultado = a * b
            print(f"\nResultado: {resultado}")

        case '/':
            logoSenai()
            resultado = a / b
            print(f"\nResultado: {resultado}")
        case _:
            logoSenai()
            print("Operador inválido.")
    
    
    print("\n\tMENU\n")
    print("1 - Fazer outra operação.")
    print("2 - Encerrar progama e sair.\n")

    continua = int(input("Digite o numero da opção desejada: "))

    match continua:

        case 1:
            logoSenai()
        case 2:
            logoSenai()
            print("Encerrando progama...")
            break
        case _:
            logoSenai()
            print("Opção inválida.")