import os
os.system("cls||clear")

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
estadoCivil = input("Digite seu estado cívil: ")
sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == 'f' or sexo == "feminino" and estadoCivil == "casada":
    tempoCasamento = int(input("Digite seu tempo de casada (anos): "))

print(f"\nNome: {nome}")

if sexo == 'f' or sexo == "feminino":
    print("Sexo: Feminino")
    if estadoCivil == "casada":
        print("Estado cívil: Casada")
    else:
        print("Estado cívil: Solteira")    
else:
    print("Sexo: Masculino")
    if estadoCivil == "casado":
        print("Estado cívil: Casado")
    else:
        print("Estado cívil: Solteiro")     

if sexo == 'f' or sexo == "feminino" and estadoCivil == "casada":
    print(f"Tempo de casamento: {tempoCasamento} anos.")