import os
os.system("cls||clear")

i = 0
contadorPares = 0
contadorImpares = 0
somaPares = 0
somaGeral = 0
numerosPares = 0

while True:

    numero = int(input("Digite um número: "))

    if numero == 0:
     
        print("\nLeitura encerrada.")
        break
    
    else:
       
        i += 1
        somaGeral += numero

        if numero % 2 == 0:
        
            contadorPares += 1
            somaPares += numero
        
        else:

            contadorImpares += 1

print(f"\nQuantidade de números pares: {contadorPares}")
print(f"Quantidade de números ímpares: {contadorImpares}")

if contadorPares != 0:
    mediaPares = somaPares / contadorPares
    print(f"Média dos números pares: {mediaPares}")

mediaGeral = somaGeral / i
print(f"Média geral: {mediaGeral}")