import os
os.system("cls||clear")

mulheresSalario5k = 0
somaSalario = 0
maiorIdade = 0
menorIdade = 999
i = 0

while True:
    
    print("\nCódigo|\tDescrição")
    print("1|\tAdicionar Pessoa")
    print("2|\tExibir resultados")

    opcao = input("\nDigite o número da opção correspondente: ")

    match opcao:

        case '1':

            i += 1
            idade = int(input("Digite sua idade: "))
                
            while idade < 0:
               
                os.system("cls||clear")
                print("\nIdade inválida")
          
            salario = int(input("Digite seu salário: "))

            while salario < 0:

                os.system("cls||clear")
                print("\nSalário inválido.")    

            sexo = input("Digite seu sexo: ")
            sexo = sexo.upper()
                    
            while sexo != 'M' and sexo != 'F':

                 os.system("cls||clear")
                 print("\nSexo inválido")

            somaSalario += salario

            if idade > maiorIdade:

                maiorIdade = idade

            if idade < menorIdade:

                menorIdade = idade

            if sexo == 'f' and salario >= 5000:

                mulheresSalario5k += 1     

        case '2':

            if i == 0:
                os.system("cls||clear")
                print("\nNenhuma pessoa adicionada.")
                break

            else:

                print(f"Mulheres com salário acima de R$ 5.000: {mulheresSalario5k}")
                print(f"Maior idade: {maiorIdade}")
                print(f"Menor idade: {menorIdade}")
                mediaSalarial = somaSalario / i
                print(f"Média salarial: {mediaSalarial}")

        case _:
            os.system("cls||clear")
            print("\nOpção inválida.")
            

            