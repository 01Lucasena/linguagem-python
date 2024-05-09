import os
os.system("cls||clear")

QUANTIDADE_DE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_DE_NOTAS):

    while True:
        
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            
            print("\nNota inválida, digite novamente.\n")
        
        else:

            soma += nota
            break

media = soma / QUANTIDADE_DE_NOTAS

print(f"\nMédia: {media}")

if media >= 7:
    
    print("Aprovado.")

elif media >= 5 and  media < 7:

    print("Recuperação.")

else:

    print("Reprovado.")