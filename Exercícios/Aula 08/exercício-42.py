import os

def logoSenai():
    os.system("cls||clear")
    print("\t===========")
    print("\t===SENAI===")
    print("\t===========\n")

logoSenai()

while True:
    print("\nCÓDIGO\t\tPRATO\t\tVALOR\n")
    print("1\t\tPicanha\t\tR$25,00")
    print("2\t\tLasanha\t\tR$20,00")
    print("3\t\tStrogonoff\tR$18,00")
    print("4\t\tBife acebolado\tR$15,00")
    print("5\t\tPão c/ ovo\tR$5,00\n")

    codigo = int(input("Digite o código do prato: "))

    match codigo:

        case 1:
            print("\nPicanha - R$25,00")
            break
        case 2:
            print("\nLasanha - R$20,00")
            break
        case 3:
            print("\nStrogonoff - R$18,00")
            break
        case 4:
            print("\nBife acebolado - R$15,00")
            break
        case 5:
            print("\nPão com ovo - R$5,00")
            break
        case _:
            print("\nOpção inválida")