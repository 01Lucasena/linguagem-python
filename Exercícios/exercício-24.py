import os
os.system("cls||clear")

i = 0
soma = 0

while True:

    print("\tMENU\t")
    print("\nS - Inserir mais uma nota")
    print("\nP - Ver quantas notas foram inseridas")
    print("\nN - Calcular a média aritimética das notas informadas\n")

    opcao = input("Digite a letra que corresponde a opção desejada: ")

    opcao = opcao.lower()

    match opcao:

        case 's':

            i += 1
            nota = float(input("\nInsira uma nota: "))
            soma += nota
        
        case 'p':

            print(f"Quantidade de notas inseridas: {i}")
        
        case 'n':

            if i == 0:
                print("\nNenhuma nota inserida.")
                break

            else:
                media = soma / i
                print(f"Média: {media}")
                break
        
        case _:

            print("Opção inválida")