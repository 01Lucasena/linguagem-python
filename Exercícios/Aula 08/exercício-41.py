import os

def logoSenai():
    os.system("cls||clear")
    print("\t===========")
    print("\t===SENAI===")
    print("\t===========\n")

logoSenai()
print("\n\tINDICADOR DE DIA ÚTIL\n")
print("1 - Domingo")
print("2 - Segunda - feira")
print("3 - Terça - feira")
print("4 - Quarta - feira")
print("5 - Quinta - feira")
print("6 - Sexta - feira")
print("7 - Sábado\n")

opcao = int(input("Digite o número da operação desejada: "))

match opcao:

    case 1:
        print("\nDomingo - Final de semana.")
    case 2:
        print("\nSegunda-feira - É dia útil.")
    case 3:
        print("\nTerça-feira - É dia útil.")
    case 4:
        print("\nQuarta-feira - É dia útil.")
    case 5:
        print("\nQuinta-feira - É dia útil.")
    case 6:
        print("\nSexta-feira - É dia útil.")
    case 7:
        print("\nSábado - Final de semana.")
    case _:
        print("\nOpção inválida.")